![](https://github.com/stsuberi/SaraTest/blob/master/cloudshell_logo.png)

# ByteBlower Chassis 2G Shell

Release date: May 2022

Shell version: 3.2.0

Document version: 1.2.3

# In This Guide

* [Overview](#overview)
* [Downloading the Shell](#downloading-the-shell)
* [Importing and Configuring the Shell](#importing-and-configuring-the-shell)
* [Updating Python Dependencies for Shells](#updating-python-dependencies-for-shells)
* [References](#references)
* [Release Notes](#release-notes)

# Overview
A shell integrates a device model, application or other technology with CloudShell. A shell consists of a data model that defines how the device and its properties are modeled in CloudShell, along with automation that enables interaction with the device via CloudShell.

### Traffic Generator Shells
CloudShell's traffic generator shells enable you to conduct traffic test activities on Devices Under Test (DUT) or Systems Under Test (SUT) from a sandbox. In CloudShell, a traffic generator is typically modeled using a chassis resource, which represents the traffic generator device and ports, and a controller service that runs the chassis commands, such as Load Configuration File, Start Traffic and Get Statistics. Chassis and controllers are modeled by different shells, allowing you to accurately model your real-life architecture. For example, scenarios where the chassis and controller are located on different machines.

For additional information on traffic generator shell architecture, and setting up and using a traffic generator in CloudShell, see the [Traffic Generators Overiew](http://help.quali.com/Online%20Help/9.0/Portal/Content/CSP/LAB-MNG/Trffc-Gens.htm?Highlight=traffic%20generator%20overview) online help topic.

### ByteBlower Chassis 2G Shell
The ByteBlower Chassis 2G Shell provides you with connectivity and management capabilities such as device structure discovery and power management for the ByteBlower chassis. 

For more information on the ByteBlower Chassis, see the ByteBlower official product documentation.

To model an ByteBlower Chassis device in CloudShell, use one of the following controllers, which provide automation commands to run on the chassis, such as Load Configuration, Start Traffic/Test, Get Statistics: 

▪ <a href="https://github.com/QualiSystems/ByteBlower-Controller-Shell-2G" target="_blank">ByteBlower Controller Shell</a>

### Standard version
The ByteBlower Chassis 2G Shell 3.1.0 is based on the Traffic Shell standard *cloudshell_traffic_generator_chassis_standard_1_0_4.yaml*.

For detailed information about the shell’s structure and attributes, see the [Traffic Shell standard](https://github.com/QualiSystems/shell-traffic-standard/blob/master/spec/traffic_standard.md) in GitHub.

### Supported OS
▪ Windows

### Requirements

▪ CloudShell version **v2021.2.0 and up**

**Note:** If your CloudShell version does not support this shell, you should consider upgrading to a later version of CloudShell or contact customer support.

### Data Model
#### **ByteBlower Chassis Families and Models**

The chassis families and models are listed in the following table:

|Family|Model| Description          |
|:---|:---|:---------------------|
|CS_TrafficGeneratorChassis|ByteBlower Chassis Shell 2G| ByteBlower chassis   |
|CS_TrafficGeneratorModule|ByteBlower Chassis Shell 2G.GenericTrafficGeneratorModule| ByteBlower module    |
|CS_TrafficGeneratorPort|ByteBlower Chassis Shell 2G.GenericTrafficGeneratorPort| ByteBlower port      |
|CS_TrafficGeneratorPort|ByteBlower Chassis Shell 2G.ByteBlowerEndPoint| ByteBlower end-point |

#### **ByteBlower Chassis Attributes**

The attribute names and types are listed in the following table:

| Attribute                                                               |Type| Default value | Description                                                                                                                      |
|:------------------------------------------------------------------------|:---|:--------------|:---------------------------------------------------------------------------------------------------------------------------------|
| CS_TrafficGeneratorChassis.Model Name                                   |string|               | The catalog name of the ByteBlower chassis model. This attribute will be displayed in CloudShell instead of the CloudShell model. |
| CS_TrafficGeneratorChassis.Vendor                                       |string| Excentis      | The name of the ByteBlower chassis manufacture.                                                                                  |
| CS_TrafficGeneratorChassis.Version                                      |string|               | The firmware version of the ByteBlower chassis.                                                                                  |
| ByteBlower Chassis Shell 2G.Serial Number                               |string|               | The serial number of the ByteBlower chassis.                                                                                     |
| ByteBlower Chassis Shell 2G.Server Description                          |string|               | The full description of the server. Usually includes the OS, exact firmware version and additional characteritics of the device. |
| ByteBlower Chassis Shell 2G.Client Install Path                         |string|               | NA for this resource.                                                                                                            |
| ByteBlower Chassis Shell 2G.Controller Address                          |string|               | NA for this resource.                                                                                                            |
| ByteBlower Chassis Shell 2G.Meeting Point                               |string|               | The IP address of the meeting point, appliacable only when ByteBlower is using meeting point.                                    |
| ByteBlower Chassis Shell 2G.Controller TCP Port                         |string|               | NA for this resource.                                                                                                            |
| ByteBlower Chassis Shell 2G.Password                                    |string|               | NA for this resource.                                                                                                            |
| ByteBlower Chassis Shell 2G.Power Management                            |boolean| True          | Used by the power management orchestration, if enabled, to determine whether to automatically manage the device power status.    |
| ByteBlower Chassis Shell 2G.User                                        |string|               | NA for this resource.                                                                                                            |
| CS_TrafficGeneratorModule.Model Name                                    |string|               | The catalog name of the ByteBlower module model. This attribute will be displayed in CloudShell instead of the CloudShell model. |
| ByteBlower Chassis Shell 2G.GenericTrafficGeneratorModule.Serial Number |string|               | The serial number of the ByteBlower module.                                                                                      |
| ByteBlower Chassis Shell 2G.GenericTrafficGeneratorModule.Version       |string|               | The firmware version of the ByteBlower module.                                                                                   |
| CS_TrafficGeneratorPort.Configured Controllers                          |string|               | NA for this resource. |
| CS_TrafficGeneratorPort.Logical Name                                    |string|               | The port's logical name in the test configuration. If kept emtpy - allocation will applied in the blue print.                                                                                                                      |
| CS_TrafficGeneratorPort.Max Speed                                       |string|               | Max speed supported by the interface (default units - MB).                       |
| ByteBlower Chassis Shell 2G.CS_TrafficGeneratorPort.Media Type          |string|               | Interface media type. Possible values are Fiber and/or Copper (comma-separated). |
| ByteBlower Chassis Shell 2G.ByteBlowerEndPoint.Address                  |string|               | The IP address of the port in the traffic configuration.                                                                                      |
| ByteBlower Chassis Shell 2G.ByteBlowerEndPoint.Gateway                  |string|               | The default gateway address of the port in the traffic configuration.                                                                                      |
| ByteBlower Chassis Shell 2G.ByteBlowerEndPoint.Mac Address              |string|               | The mac address of the port in the traffic configuration.                                                                                      |
| ByteBlower Chassis Shell 2G.ByteBlowerEndPoint.Netmask                  |string|               | The netmask address of the port in the traffic configuration.                                                                                      |
| ByteBlower Chassis Shell 2G.ByteBlowerEndPoint.Address                  |string|               | The IP address of the endpoint.                                                                                      |
| ByteBlower Chassis Shell 2G.ByteBlowerEndPoint.Identifier               |string|               | The unique ID of the endpoint.                                                                                      |
| ByteBlower Chassis Shell 2G.ByteBlowerEndPoint.SSID                     |string|               | The endpoints's SSID. If kept emtpy - allocation will applied in the blue print.                                                                                      |
| ByteBlower Chassis Shell 2G.ByteBlowerEndPoint.Version                  |string|               | The endpoints's SSID. If kept emtpy - allocation will applied in the blue print.                                                                                      |

### Automation
This section describes the automation (drivers or scripts) associated with the data model. The shell’s driver is associated with the model and provided as part of the shell package).There are two types of automation processes, Autoload and Resource. Autoload is executed when creating the resource in the Inventory dashboard, while resource commands are run in the Sandbox, providing that the resource has been discovered and is online.

For Traffic Generator Shells, commands are configured and executed from the controller service in the sandbox, with the exception of the Autoload command, which is executed when creating the resource.

|Command|Description|
|:-----|:-----|
|Autoload|Discovers the chassis, its hierarchy and attributes when creating the resource. The command can be rerun in the Inventory dashboard and not in the sandbox, as for other commands.|

### Downloading the Shell
The ByteBlower Chassis 2G Shell is available from the [Quali Community Integrations](https://community.quali.com/integrations) page. 

Download the files into a temporary location on your local machine. 

The shell comprises:

|File name|Description|
|:---|:---|
|ByteBlower.Chassis.Shell.2G.zip|ByteBlower Chassis Shell package|
|ByteBlower.Chassis.Shell.2G.ByteBlower.requirements.zip|Shell Python dependencies (for offline deployments only)|

# Importing and Configuring the Shell
This section describes how to import the ByteBlower Chassis 2G Shell and configure and modify the shell’s devices.

### Importing the shell into CloudShell

**To import the shell into CloudShell:**
  1. Make sure you have the shell’s zip package. If not, download the shell from the [Quali Community's Integrations](https://community.quali.com/integrations) page.
  2. In CloudShell Portal, as Global administrator, open the **Manage – Shells** page.
  3. Click **Import**.
  4. In the dialog box, navigate to the shell's zip package, select it and click **Open**.

The shell is displayed in the **Shells** page and can be used by domain administrators in all CloudShell domains to create new inventory resources, as explained in [Adding Inventory Resources](http://help.quali.com/Online%20Help/9.0/Portal/Content/CSP/INVN/Add-Rsrc-Tmplt.htm?Highlight=adding%20inventory%20resources). 

### Offline installation of a Shell

**Note:** Offline installation instructions are relevant only if CloudShell Execution Server has no access to PyPi. You can skip this section if your execution server has access to PyPi. For additional information, see the online help topic on offline dependencies.

In offline mode, import the shell into CloudShell and place any dependencies in the appropriate dependencies folder. The dependencies folder may differ, depending on the CloudShell version you are using:

### Adding Shell and script packages to the local PyPi Server repository
If your Quali Server and/or execution servers work offline, you will need to copy all required Python packages, including the out-of-the-box ones, to the PyPi Server's repository on the Quali Server computer (by default *C:\Program Files (x86)\QualiSystems\CloudShell\Server\Config\Pypi Server Repository*).

For more information, see [Configuring CloudShell to Execute Python Commands in Offline Mode](http://help.quali.com/Online%20Help/9.0/Portal/Content/Admn/Cnfgr-Pyth-Env-Wrk-Offln.htm?Highlight=Configuring%20CloudShell%20to%20Execute%20Python%20Commands%20in%20Offline%20Mode).

**To add Python packages to the local PyPi Server repository:**
  1. If you haven't created and configured the local PyPi Server repository to work with the execution server, perform the steps in [Add Python packages to the local PyPi Server repository (offlinemode)](http://help.quali.com/Online%20Help/9.0/Portal/Content/Admn/Cnfgr-Pyth-Env-Wrk-Offln.htm?Highlight=offline%20dependencies#Add). 
  2. For each shell or script you add into CloudShell, do one of the following (from an online computer):
      * Connect to the Internet and download each dependency specified in the *requirements.txt* file with the following command: 
`pip download -r requirements.txt`. 
     The shell or script's requirements are downloaded as zip files.

      * In the [Quali Community's Integrations](https://community.quali.com/integrations) page, locate the Shell and click the Shell's **Download** link. In the page that is displayed, from the Downloads area, extract the dependencies package zip file.

3. Place these zip files in the local PyPi Server repository.
 
### Setting the python PythonOfflineRepositoryPath configuration key
Before PyPi Server was introduced as CloudShell’s python package management mechanism, the `PythonOfflineRepositoryPath` key was used to set the default offline package repository on the Quali Server machine, and could be used on specific Execution Eerver machines to set a different folder. 

**To set the offline python repository:**
1. Download the *ByteBlower.Chassis.Shell.2G.offline.requirements.zip* file, see [Downloading the Shell](#downloading-the-shell).
2. Unzip it to a local repository. Make sure the execution server has access to this folder. 
3.  On the Quali Server machine, in the *~\CloudShell\Server\customer.config* file, add the following key to specify the path to the default python package folder (for all Execution Servers):  
	`<add key="PythonOfflineRepositoryPath" value="repository 
full path"/>`
4. If you want to override the default folder for a specific Execution Server, on the Execution Server machine, in the *~TestShell\Execution Server\customer.config* file, add the following key:  
	`<add key="PythonOfflineRepositoryPath" value="repository 
full path"/>`
5. Restart the Execution Server.

### Configuring a new resource
This section explains how to create a new resource from the shell.

In CloudShell, the component that models the device is called a resource. It is based on the shell that models the device and allows the CloudShell user and API to remotely control the device from CloudShell.

You can also modify existing resources, see [Managing Resources in the Inventory](http://help.quali.com/Online%20Help/8.3/Portal/Content/CSP/INVN/Mng-Rsrc-in-Invnt.htm?Highlight=managing%20resources).

**To create a resource for the device:**
  1. In the CloudShell Portal, in the **Inventory** dashboard, click **Add New**. 
     ![](https://github.com/stsuberi/SaraTest/blob/master/create_a_resource_device.png)
  2. From the list, select the **ByteBlower Chassis 2G Shell**.
  3. Enter the **Name** and **IP address** of the ByteBlower Chassis.
  4. Click **Create**.
  5. Click **Continue**.

CloudShell validates the device’s settings and updates the new resource with the device’s structure (if the device has a structure).

# Updating Python Dependencies for Shells
This section explains how to update your Python dependencies folder. This is required when you upgrade a shell that uses new/updated dependencies. It applies to both online and offline dependencies.

### Updating offline Python dependencies
**To update offline Python dependencies:**
1. Download the latest Python dependencies package zip file locally.
2. Extract the zip file to the suitable offline package folder(s). 
3. Restart any execution server that has a live instance of the relevant driver or script. This requires running the Execution Server's configuration wizard, as explained in the [Configure the Execution Server](http://help.quali.com/doc/9.0/CS-Install/content/ig/configure%20cloudshell%20products/cfg-ts-exec-srver.htm?Highlight=configure%20the%20execution%20server) topic of the CloudShell Suite Installation guide. 

### Updating online Python dependencies
In online mode, the execution server automatically downloads and extracts the appropriate dependencies file to the online Python dependencies repository every time a new instance of the driver or script is created.

**To update online Python dependencies:**
* If there is a live instance of the shell's driver or script, restart the execution server, as explained above. If an instance does not exist, the execution server will download the Python dependencies the next time a command of the driver or script runs.

# References
To download and share integrations, see [Quali Community's Integrations](https://community.quali.com/integrations). 

For instructional training and documentation resources, see the [Quali University](https://www.quali.com/university/).

To suggest an idea for the product, see [Quali's Idea box](https://community.quali.com/ideabox). 

To connect with Quali users and experts from around the world, ask questions and discuss issues, see [Quali's Community forums](https://community.quali.com/forums). 

To use traffic generator ports as abstract resources, see [CloudShell's Online Help](https://help.quali.com/Online%20Help/9.1/Portal/Content/CSP/LAB-MNG/Traffic-Gens-Abst.htm?Highlight=traffic%20generator).

# Release Notes
### What's New

* Sets unknown port speed to zero.
* Supports new card types.
* Displays only active ports instead of all ports.

### Known Issues
* Resource groups are not modeled. Resource groups are modeled as ports with a speed that represents the total speed of the group. The index of the represented port is the index of the active port of the group.
