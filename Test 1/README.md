# bik_rent_room

## Overview
`bik_rent_room` is a custom Odoo module designed for managing room rentals. This module enables users to organize, manage, and track room booking activities directly within the Odoo environment.

## Features
- Room management and availability tracking
- Booking and rental details management
- Customizable to fit specific rental requirements

## Installation Guide

### Prerequisites
- Odoo 17 installed
- Python 3.8+ environment (recommended)
- Ensure `bik_rent_room` addon files are accessible

### Installation Steps

1. **Download or Clone the Module**
   Download or clone the `bik_rent_room` repository into your Odoo addons directory:

   ```bash
   git clone https://github.com/bayuik/bik_rent_room.git
   ```

2. **Update Module List**
   Log into your Odoo instance as an administrator, navigate to the **Apps** menu, and click on **Update Apps List** to refresh the list of available addons.

3. **Install the Module**
   In the Apps menu, search for `bik_rent_room` and click **Install** to add it to your Odoo instance.

4. **Configure Settings (Optional)**
   After installation, you may need to adjust settings to match your rental requirements. Go to the module configuration under the `Settings` or `Configuration` menu.

### Updating the Module
If there are updates to `bik_rent_room`:
1. Pull the latest changes in the addon directory:
   ```bash
   git pull origin main
   ```
2. Restart the Odoo service:
   ```bash
   sudo service odoo restart
   ```
3. Upgrade the module in Odoo via the **Apps** menu or using the Odoo shell.

## Usage
Navigate to the `bik_rent_room` module from the main menu to start managing room rentals. Explore the features to add rooms, create bookings, and view rental records.
