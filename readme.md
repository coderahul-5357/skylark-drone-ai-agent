# Skylark Drone Operations AI Agent

## Overview

This project implements an AI-driven Drone Operations Coordinator system for Skylark Drones.

The system automates:
- Pilot roster management
- Mission assignment coordination
- Drone inventory tracking
- Conflict detection
- Urgent reassignment handling

Built as a full stack web application using FastAPI and Google Sheets as the live operational database.

---

## Architecture

Frontend:
- HTML Dashboard UI
- Sidebar-based operations panel
- Conversational AI interface

Backend:
- FastAPI server
- Rule-based AI decision engine

Database:
- Google Sheets (2-way sync)
- Pilot Roster
- Drone Fleet
- Missions

Deployment:
- Railway / Render cloud hosting

---

## Core Features

### Roster Management
- Query pilot availability by skill and location
- Update pilot status (syncs to Google Sheets)
- View assignment state

### Assignment Engine
- Match pilots to missions
- Drone compatibility filtering
- Weather-based filtering

### Drone Inventory
- Query by capability
- Maintenance detection
- Deployment status tracking

### Conflict Detection
- Skill mismatch warnings
- Location mismatch alerts
- Maintenance conflicts
- Weather risk alerts
- Double booking detection

### Urgent Reassignment
- Priority-based override logic
- Automatic availability search

---

## Tech Stack

- Python 3
- FastAPI
- Google Sheets API
- HTML / CSS
- Uvicorn

---

## Setup (Local)

1. Clone the repository
2. Create virtual environment
3. Install dependencies:

