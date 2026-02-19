# import os 
# from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse, JSONResponse
# from fastapi.templating import Jinja2Templates

# from sheets import read_sheet, update_pilot_status
# from logics import find_available_pilots, suggest_replacement

import os
import re
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from sheets import read_sheet, update_pilot_status
from logics import find_available_pilots
from logics import detect_conflicts


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

print("Template directory path:", TEMPLATE_DIR)

templates = Jinja2Templates(directory=TEMPLATE_DIR)

app = FastAPI()


app = FastAPI()

templates = Jinja2Templates(directory="templates")

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    message = data["message"].lower()

    pilots = read_sheet("pilot_roster")

    if "check conflicts" in message:
     pilots = read_sheet("pilot_roster")
     drones = read_sheet("drone_fleet")
     missions = read_sheet("missions")

    conflicts = detect_conflicts(pilots, drones, missions)

    return {"conflicts": conflicts}


    if "available pilot" in message:
        try:
            # parts = message.split("in")
            # skill = parts[0].replace("available pilot for", "").strip()
            # location = parts[1].strip()
            match = re.search(r"available pilot for (.+) in (.+)", message)
            if match:
                skill = match.group(1).strip()
                location = match.group(2).strip()
            else:
                return {"error": "Invalid format. Try: available pilot for Mapping in Bangalore"}      
            
            result = find_available_pilots(pilots, skill, location)

            return JSONResponse(result.to_dict(orient="records"))

        except:
            return {"error": "Invalid format. Try: available pilot for Mapping in Bangalore"}

    if "update status" in message:
        try:
            parts = message.split()
            pilot_name = parts[2]
            new_status = parts[3]

            success = update_pilot_status(pilot_name, new_status)
            return {"status_updated": success}

        except:
            return {"error": "Format: update status Arjun Available"}

    return {"message": "Command not recognized"}
