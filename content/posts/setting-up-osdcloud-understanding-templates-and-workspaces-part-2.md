---
title: "Setting Up OSDCloud: Understanding Templates and Workspaces (Part 2)"
description: ""
pubDate: "2024-11-01 20:44:25"
updatedDate: "2025-11-28 15:52:44"
slug: "setting-up-osdcloud-understanding-templates-and-workspaces-part-2"
draft: true
categories: []
  - "osdcloud"
  - "powershell"
tags: []
wordpress_id: "366"
original_url: "https://using-it.dk/setting-up-osdcloud-understanding-templates-and-workspaces-part-2/"
---

Certainly, here’s an enhanced version with more code examples to illustrate each step.

**OSDCloud Setup Guide: Templates and Workspaces**

In **OSDCloud**, **Templates** and **Workspaces** are the foundational building blocks that bring structure and flexibility to your Windows deployment process. Here’s a comprehensive guide to what they are, why they’re essential, and how to set them up effectively.

**1. OSDCloud Template: The Blueprint for Your Deployments**

An **OSDCloud Template** is a base configuration that defines language, locale, and core settings for your Windows Preinstallation Environment (WinPE). Using Templates ensures every deployment is standardized and simplifies the creation of custom environments.

**Why Use a Template?**

• **Standardization:** Ensures all deployments share the same base settings (e.g., language, keyboard layout).

• **Reusability:** Serves as a foundation, enabling easy replication without redoing core setup each time.

• **Consistency:** Creates a reliable starting point for all Workspaces, ensuring predictable deployment configurations.

**Creating an OSDCloud Template**

To create a Template, open PowerShell and run:

`New-OSDCloudTemplate -Language da-dk -SetInputLocale da-dk`

*Replace *da*-dk** with the language and input locale you need.*

**Template Options and Configurations**

You can further refine your template with these options:

• **Custom Language:**

`New-OSDCloudTemplate -Language fr-FR -SetInputLocale fr-FR`

*Sets the language and keyboard to French (France).*

• **Multiple Keyboard Layouts:**

`New-OSDCloudTemplate -Language en-US -SetInputLocale en-US,de-DE`

*Adds both US and German keyboard layouts.*

• **Specifying a Time Zone:**

`New-OSDCloudTemplate -Language en-US -SetInputLocale en-US -TimeZone "Central Standard Time"`

*Sets Central Standard Time for deployments.*

**What’s Inside the Template?**

The Template configures essential deployment settings, such as:

• **Regional and Language Settings:** Ensures consistent locale for all deployments.

• **Network Setup:** Configures network for smooth connectivity in the WinPE environment.

**Tip:** The Template itself is not deployed; rather, it’s used to create a customized Workspace that you’ll deploy.

**2. OSDCloud Workspace: Customizing Each Deployment**

Once you have your Template, you can create a **Workspace**—a working directory derived from the Template, where all deployment-specific configurations live. Workspaces allow for unique customizations per deployment, such as adding drivers, branding, or specific scripts.

**Why Use a Workspace?**

• **Customization:** Tailor each Workspace to fit specific hardware, software, or environment requirements.

• **Organized Structure:** Keeps drivers, scripts, and media files organized and easily accessible.

• **Modularity:** Each Workspace can be updated without altering the Template, keeping base settings intact.

**Creating an OSDCloud Workspace**

To set up a Workspace from the Template, run:

`New-OSDCloudWorkspace -WorkspacePath C:\OSDCloud`

*Replace **C:\OSDCloud** with your chosen directory path.*

**Inside the Workspace**

Your Workspace directory will have folders for specific types of configurations:

• **Media:** For OS installation files.

• **Drivers:** Add drivers here to ensure compatibility with specific hardware.

• **Scripts:** Store PowerShell or batch scripts to run at various stages of deployment.

• **Configurations:** Pulls in language and regional settings from your Template.

**Workspace Customization Examples**

1. **Adding Drivers for Specific Hardware Models**

• For example, if deploying on Dell and Lenovo machines, download and place their drivers in the Drivers folder:

`Edit-OSDCloudWinPE -CloudDriver Dell,Lenovo`

• This will download and inject the latest drivers into the Workspace’s WinPE environment.

2. **Adding a Custom Wallpaper**

• To set a custom wallpaper in the WinPE environment:

`Edit-OSDCloudWinPE -Wallpaper "C:\Path\To\Wallpaper.jpg"`

• Place your wallpaper image in the specified path. This image will display during setup, providing a branded experience.

3. **Including Custom PowerShell Scripts**

• For tasks like installing specific applications or configurations, include PowerShell scripts by placing them in the Scripts folder:

`Edit-OSDCloudWinPE -WebPSScript "https://yourdomain.com/scripts/setup.ps1"`

• This script will automatically run during deployment, allowing you to customize settings on the deployed machine.

**Creating Bootable Media from the Workspace**

Once your Workspace is configured, you can create bootable media for deployment:

• **USB Drive:**

`New-OSDCloudUSB -WorkspacePath C:\OSDCloud`

*Inserts and formats a USB drive to create a bootable deployment media.*

• **ISO File:**

`New-OSDCloudISO -WorkspacePath C:\OSDCloud`

*Generates an ISO for virtual machines or other boot methods.*

**Summary: Templates and Workspaces in OSDCloud**

• **Template:** Your base setup defining language, locale, and timezone. Created once, used across multiple deployments.

• **Workspace:** A customizable environment derived from the Template, where you add specific drivers, scripts, and configurations for each deployment scenario.

Using Templates and Workspaces gives you a modular, efficient approach to Windows deployment with OSDCloud, allowing you to quickly adapt to different hardware and scenarios while maintaining a consistent core setup.

**Next Steps:** Now that you’ve created a Template and Workspace, you’re ready to explore further customization and advanced deployment scenarios in upcoming posts!