---
title: "Why Use PSAppDeployToolkit with SCCM or Intune?"
description: ""
pubDate: "2023-09-26 13:33:21"
updatedDate: "2025-11-28 15:04:38"
slug: "why-use-psappdeploytoolkit-with-sccm-and-intune"
draft: true
categories: []
  - "intune"
  - "powershell"
tags: []
wordpress_id: "240"
original_url: "https://using-it.dk/why-use-psappdeploytoolkit-with-sccm-and-intune/"
---

<ol>
- **Unified Application Deployment**: PSAppDeployToolkit (PSADT) provides a standardized method for application deployment, allowing for consistent experiences across different platforms and deployment methodologies. By integrating it with SCCM and Intune, you can maintain a uniform deployment procedure whether you're managing on-premises devices or cloud-based ones.

- **Enhanced User Experience**: PSADT offers a customizable user interface for deployments, ensuring that end users are informed about the software changes on their devices. This fosters better user acceptance and reduces potential helpdesk calls due to unexpected software changes or restarts.

- **Robust Logging**: With detailed logging features, PSADT can provide granular insights into the deployment process. This is invaluable for troubleshooting and ensures that administrators can quickly identify and rectify any issues.

- **Extended Functionality**: Beyond just software deployment, PSADT comes with a plethora of additional functionalities, such as checking prerequisites, closing specific applications before an installation, and more. This means that complex deployment scenarios can be managed more effectively.

- **Seamless Integration**: Both SCCM and Intune support PowerShell scripting, making it straightforward to integrate PSADT. This ensures that you can leverage the strengths of PSADT while still benefiting from the management capabilities of SCCM and Intune.

- **Cost-Efficient**: PSAppDeployToolkit is a free tool. By utilizing it with SCCM and Intune, organizations can potentially reduce the costs associated with purchasing third-party application packaging and deployment solutions.

- **Community Support**: Given its popularity in the IT Pro community, there's a plethora of resources, guides, and community support available for PSAppDeployToolkit. This community-driven approach ensures that the tool stays relevant and continues to evolve with the changing IT landscape.
</ol>

In conclusion, when you're aiming for a seamless, efficient, and user-friendly application deployment process, integrating PSAppDeployToolkit with SCCM and Intune becomes an attractive proposition. It bridges the gap between complex deployment requirements and the need for a consistent user experience, ensuring that IT teams can deploy applications effectively while minimizing disruptions for end-users.

### PSAppDeployToolkit (PSADT): Usage and Customization Guide

**1. Download and Extract:** First, download the latest version of the toolkit from its official repository. Once downloaded, extract the files to a location of your choice.

**2. Exploring the Toolkit:** You'll notice that the main components are:

- `Deploy-Application.ps1`: The main script where you define the installation and uninstallation process.

- `AppDeployToolkit`: Contains core scripts and functions of the toolkit.

- `Deploy-Application.exe`: A stub executable to launch the main script.

- `Files`: A directory to place installer files (like .msi or .exe files).

- `SupportFiles`: A directory for additional resources like logos or configuration files.

**3. Customizing the Configuration:** Navigate to `AppDeployToolkit\AppDeployToolkitConfig.xml`. This XML file is where you can define your application name, modify the UI, set the toolkit's behavior, and more.

**4. Writing the Installation Logic:**

Edit the `Deploy-Application.ps1` script. The main sections you'll focus on are:

- **Pre-Installation**: Any actions to perform before installing the new software. You can close specific applications, check prerequisites, or uninstall previous versions here.

- **Installation**: Where you define how the software gets installed. You can run the installer silently, wait for the process to complete, and more.

- **Post-Installation**: Any actions after the installation, like cleaning up temporary files or starting services.

**5. Customizing User Prompts:**

To display messages or prompts to the user, use the `Show-InstallationPrompt` command. For example:

powershellCopy code

`Show-InstallationPrompt -Message "Please close Microsoft Word to continue the installation" -ButtonRightText "Continue" -Icon Information`

**6. Adding Logos and Branding:**

To customize the branding, replace the banner and icon in the `SupportFiles` folder with your corporate branding. The toolkit will use these for the UI prompts.

**7. Testing the Deployment:**

Always test the script to ensure it behaves as expected. You can run `Deploy-Application.ps1` in different modes:

- Install: `Deploy-Application.ps1 -DeploymentType "Install"`

- Uninstall: `Deploy-Application.ps1 -DeploymentType "Uninstall"`

- Repair: `Deploy-Application.ps1 -DeploymentType "Repair"`

**8. Deployment with SCCM or Intune:**

- **SCCM**: Create a package or an application in SCCM, point the source files to the directory where you have the PSADT files, and use `Deploy-Application.exe` as the main executable for the deployment.

- **Intune**: For Intune, you might need to wrap the toolkit and the installer into an `.intunewin` package using the Intune Win32 App Packaging Tool. Then, upload this package to Intune for deployment.

<hr class="wp-block-separator has-alpha-channel-opacity"/>

Keep in mind that the PSAppDeployToolkit is powerful and offers a lot of customization. This guide is a basic overview. You might want to dive into the toolkit's documentation and community forums for more advanced scenarios or troubleshooting.

Remember, always test your deployments thoroughly in a controlled environment before rolling out to production!

Please see more info at the official website:

[PSAppDeployToolkit](https://psappdeploytoolkit.com/)