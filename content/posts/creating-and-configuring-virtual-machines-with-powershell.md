---
title: "Creating and Configuring Virtual Machines with PowerShell"
description: ""
pubDate: "2023-09-19 09:42:19"
updatedDate: "2025-11-22 21:07:58"
slug: "creating-and-configuring-virtual-machines-with-powershell"
draft: false
categories:
  - "hyper-v"
  - "powershell"
tags:
wordpress_id: "165"
original_url: "https://using-it.dk/creating-and-configuring-virtual-machines-with-powershell/"
---

If you've ever set up a LAB-environment, you'll understand the importance of automating the provisioning of infrastructure. Today, I'm going to break down a PowerShell script that allows you to automate the creation and configuration of virtual machines (VMs) based on user-defined parameters.

### What the Script Does

<ol>
- **Gathers User Input:** This script prompts users for:
</ol>

- The VM's name.

- Its size (options range from small to super-sized).

- The DVD drive option, allowing the user to choose from various installation sources or even opt for no installation media.

<ol>
- **Defines Constants:** These are fixed values such as the path for the virtual hard disk (VHD) and the VM, the switch name, and the generation of the VM.

- **Sets VM Parameters:** Depending on the user's choice of VM size, the script will allocate resources such as RAM, disk size, and the number of virtual CPUs (vCPUs).

- **Configures the DVD Drive:** The DVD drive's path will be set based on the user's choice, allowing for different operating system installations.

- **Creates and Configures the VM:** The VM will be created using the `New-VM` cmdlet, with further configurations applied post-creation such as setting the number of processors with `Set-VMProcessor`.

- **Configures Additional VM Settings:** If a DVD drive option was chosen, the script adds the drive using `Add-VMDvdDrive` and sets boot preferences. It also sets memory configurations with the `Set-VMMemory` cmdlet.
</ol>

### Walkthrough

Here's a brief step-by-step walkthrough of the script:

#### User Input:

```
$name = Read-Host "Enter the name of the VM"
$size = Read-Host "Enter the size of the VM: ..."
$dvdOption = Read-Host "Select the DVD drive option: ..."
```

The script starts by collecting essential information from the user.

#### Define Constants:

```
$vhdPath = "E:\LAB\$name\$name.vhdx"
$vmPath = "E:\LAB\"
$switchName = "HYD-CorpNet"
$gen = 2
```

These constants will be used when creating the VM, defining where to store files and which network to connect to.

#### VM Size Configuration:

The `switch` statement is used to define VM parameters like RAM, disk space, and vCPUs based on the user's size choice.

#### DVD Drive Configuration:

Another `switch` statement is used to determine which ISO image (if any) should be mounted to the VM's DVD drive.

#### VM Creation:

```
New-VM -Name $name -Path $vmPath -Generation $gen -SwitchName $switchName -MemoryStartupBytes $ram -NewVHDPath $vhdPath -NewVHDSizeBytes $disk
```

This cmdlet creates a new VM with the specified parameters.

#### Final Configurations:

The last sections of the script configure the VM's processors, DVD drive (if one was chosen), and dynamic memory settings.

#### Final script:

```
#Prompt for user input

$name = Read-Host "Enter the name of the VM"
$action = Read-Host "Select an action:
1. Create VM
2. Delete VM
Enter option number (1 or 2)"

if ($action -eq "1") {
    $size = Read-Host "Enter the size of the VM:
    1. Small (2GB RAM, 20GB disk, 4 vCPUs) (Kan IKKE køre Win11!)
    2. Medium (4GB RAM, 50GB disk, 4 vCPUs)
    3. Large (8GB RAM, 100GB disk, 8 vCPUs)
    4. Extra Large (16GB RAM, 100GB disk, 8 vCPUs)
    5. Super Size (32GB RAM, 100GB disk, 16 vCPUs)
    Enter option number (1, 2, 3, 4, or 5)"
    $dvdOption = Read-Host "Select the DVD drive option:
    1. Option1
    2. Option2
    3. Option3
    4. Option4
    Enter option number (1, 2, 3, or 4)"
    
    #Define constants

    $vhdPath = "E:\LAB\$name\$name.vhdx"
    $vmPath = "E:\LAB\"
    $switchName = "HYD-CorpNet"
    $gen = 2
    
    #Validate size input and set VM parameters

    switch ($size) {
        "1" { $ram = "2GB"; $disk = "20GB"; $vcpus = 4; }
        "2" { $ram = "4GB"; $disk = "50GB"; $vcpus = 4; }
        "3" { $ram = "8GB"; $disk = "100GB"; $vcpus = 8; }
        "4" { $ram = "16GB"; $disk = "100GB"; $vcpus = 8; }
        "5" { $ram = "32GB"; $disk = "100GB"; $vcpus = 16; }
        default { Write-Host "Invalid option. Defaulting to Medium (4GB RAM, 50GB disk, 4 vCPUs)"; $ram = "4GB"; $disk = "50GB"; $vcpus = 4; }
    }
    
    #Validate DVD drive input and set DVD path

    switch ($dvdOption) {
        "1" { $isoPath = "D:XXX.iso" }
        "2" { $isoPath = "D:XXX.iso" }
        "3" { $isoPath = "D:XXX.iso" }
        "4" { $isoPath = $null }
        default { Write-Host "Invalid option. Defaulting to None"; $isoPath = $null }
    }
    
    #Create and configure VM

    New-VM -Name $name -Path $vmPath -Generation $gen -SwitchName $switchName -MemoryStartupBytes $ram -NewVHDPath $vhdPath -NewVHDSizeBytes $disk
    Set-VMProcessor -VMName $name -Count $vcpus
    
    #Add DVD drive if applicable

    if ($isoPath) {
        Add-VMDvdDrive -VMName $name -Path $isoPath
        Set-VMFirmware -VMName $name -FirstBootDevice (Get-VMDvdDrive -VMName $name) -EnableSecureBoot On
    }
    
    Set-VMMemory -VMName $name -DynamicMemoryEnabled $true -MinimumBytes 512MB -MaximumBytes $ram
    
    Enable-VMTPM -VMName $name
}
elseif ($action -eq "2") {
    $confirm = Read-Host "Are you sure you want to delete the VM '$name'? (Y/N)"
    if ($confirm -eq "Y" -or $confirm -eq "y") {
        Remove-VM -Name $name -Force
        Write-Host "VM '$name' has been deleted."
    }
    else {
        Write-Host "VM deletion cancelle."
    }
}
else {
    Write-Host "Invalid option. Please select either 1 or 2."
}
```

### Conclusion

Automation is a boon for lab environments, ensuring consistent configurations while saving time. The PowerShell script we've discussed provides a structured, user-friendly method for VM creation and configuration. By understanding and utilizing scripts like this, you can improve the efficiency of your infrastructure setup, making it easier to manage and expand as needed.