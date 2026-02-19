from datetime import datetime

def find_available_pilots(pilots_df, skill, location):
    return pilots_df[
        (pilots_df["skills"].str.contains(skill, case=False)) &
        (pilots_df["location"] == location) &
        (pilots_df["status"] == "Available")
    ]


def calculate_pilot_cost(pilot, start_date, end_date):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    days = (end - start).days + 1
    return days * pilot["daily_rate_inr"]


def suggest_replacement(skill, location, pilots_df):
    candidates = pilots_df[
        (pilots_df["skills"].str.contains(skill, case=False)) &
        (pilots_df["status"] == "Available")
    ]

    if candidates.empty:
        return "No suitable replacement found"

    return candidates.iloc[0]["name"]

def detect_conflicts(pilots_df, drones_df, missions_df):
    conflicts = []

    for _, mission in missions_df.iterrows():
        assigned_pilot = mission.get("assigned_pilot")
        assigned_drone = mission.get("assigned_drone")

        mission_start = mission.get("start_date")
        mission_end = mission.get("end_date")
        required_skill = mission.get("required_skills")
        mission_location = mission.get("location")
        weather = mission.get("weather")

        # Pilot Checks
        if assigned_pilot:
            pilot = pilots_df[pilots_df["name"] == assigned_pilot]

            if not pilot.empty:

                # Skill mismatch
                if required_skill not in pilot.iloc[0]["skills"]:
                    conflicts.append(
                        f"Skill mismatch: {assigned_pilot} lacks {required_skill} for mission {mission['project_id']}"
                    )

                # Location mismatch
                if pilot.iloc[0]["location"] != mission_location:
                    conflicts.append(
                        f"Location mismatch: {assigned_pilot} not in {mission_location}"
                    )

        # Drone Checks
        if assigned_drone:
            drone = drones_df[drones_df["drone_id"] == assigned_drone]

            if not drone.empty:

                # Maintenance issue
                if drone.iloc[0]["status"] == "Maintenance":
                    conflicts.append(
                        f"Drone {assigned_drone} under maintenance for mission {mission['project_id']}"
                    )

                # Weather compatibility
                if weather == "Rainy" and "IP43" not in drone.iloc[0]["capabilities"]:
                    conflicts.append(
                        f"Weather risk: Drone {assigned_drone} not rain compatible"
                    )

    return conflicts
