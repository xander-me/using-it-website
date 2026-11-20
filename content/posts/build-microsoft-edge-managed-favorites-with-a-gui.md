---
title: "Build Microsoft Edge Managed Favorites with a GUI"
description: ""
pubDate: "2025-12-20 14:46:47"
updatedDate: "2025-12-29 10:04:49"
slug: "build-microsoft-edge-managed-favorites-with-a-gui"
draft: false
categories: []
  - "intune"
tags: []
wordpress_id: "557"
original_url: "https://using-it.dk/build-microsoft-edge-managed-favorites-with-a-gui/"
---

Managing browser favorites at scale sounds simple — until you actually try to do it.

If you’ve ever configured Microsoft Edge Managed Favorites via Intune, Group Policy, or custom profiles on macOS, you already know the pain points:

- Complex nested JSON structures

- No validation or visual feedback

- One missing comma = policy failure

- Different formats for Windows vs macOS/iOS

- No easy way to reorder, bulk add, or maintain structure over time

To solve this, I built a lightweight, browser-based Edge Managed Favorites Builder that lets you visually design your favorites structure and export it ready for Intune deployment.

## What Are Edge Managed Favorites?

Microsoft Edge supports centrally managed favorites through the ManagedFavorites policy.

This allows IT administrators to:

- Enforce a predefined favorites structure

- Create folders and links that appear for all users

- Keep corporate bookmarks consistent across devices

Typical use cases include:

- Corporate intranet links

- HR, payroll, and self-service portals

- IT service desks and knowledge bases

- SaaS applications and admin portals

The challenge is that ManagedFavorites is configuration-driven, not UI-driven.

**The Problem With Manual Configuration**

**1. JSON Is Fragile**

On Windows, the policy expects a very specific JSON array format.

A single syntax error breaks the entire policy.

### 2. No Visual Overview

When editing JSON directly, you have:

- No tree view

- No easy way to reorder items

- No indication of nesting depth

### 3. Platform Differences

- Windows uses a JSON array

- macOS / iOS use a plist structure

- Same logical data, different syntax

### 4. Long-Term Maintenance

Adding or reorganizing favorites later often means:

Losing consistency across platforms

Rewriting large parts of the JSON

Copy/paste errors

Losing consistency across platforms

**Introducing the Edge Managed Favorites Builder**<br><br>To remove friction from this process, I built a fully static, client-side tool that runs directly in the browser.

- No login

- No backend

- No data stored

You simply open the page, build your structure, and copy the output.

## Key Features

- Visual tree editor (folders + links)

- Unlimited nesting

- Windows and macOS/iOS output

- Bulk add links (paste from Excel or text files)

- Alphabetical sorting (A–Z), including subfolders

- Import existing Windows JSON

- Copy/paste-ready output for Intune

- Minimal, enterprise-friendly UI

## How the Tool Works (Conceptual Overview)

The tool separates **structure** from **output**.

<ol start="1" class="wp-block-list">
- You build a single logical structure:

- Folders

- Links

- Hierarchy

- The tool renders that structure into:

- Windows-compatible JSON

- Apple-compatible plist

</ol>

This guarantees:

- Identical structure across platforms

- Correct formatting every time

- No accidental policy changes

## Windows Example Output

```
[
  {
    "toplevel_name": "Company"
  },
  {
    "name": "IT",
    "children": [
      {
        "name": "Intune",
        "url": "https://intune.microsoft.com"
      },
      {
        "name": "Entra",
        "url": "https://entra.microsoft.com"
      }
    ]
  }
]
```

This output can be pasted directly into:

- Intune Settings Catalog

- Administrative Templates

- Custom OMA-URI configurations

## macOS / iOS Example Output

```
<key>ManagedFavorites</key>
<array>
  <dict>
    <key>toplevel_name</key>
    <string>Company</string>
  </dict>
  <dict>
    <key>name</key>
    <string>IT</string>
    <key>children</key>
    <array>
      <dict>
        <key>name</key>
        <string>Intune</string>
        <key>url</key>
        <string>https://intune.microsoft.com</string>
      </dict>
    </array>
  </dict>
</array>
```

This fits directly into:

- Intune Custom Configuration Profiles (macOS)

- Managed App Configuration for Edge on iOS

## Real-World Use Cases

### Enterprise IT

- Standardize favorites across hundreds or thousands of devices

- Ensure consistent access to business-critical systems

- Reduce helpdesk tickets

### Mergers &amp; Acquisitions

- Quickly reorganize bookmarks across business units

- Merge intranets and portals without chaos

### Security-Focused Environments

- Direct users to approved systems only

- Reduce reliance on user-created bookmarks

### Multi-Platform Management

- One design → multiple outputs

- Avoid platform drift over time

## Why Alphabetical Sorting Matters

In large environments, favorites tend to grow quickly.

Built-in **A–Z sorting**:

- Keeps structures readable

- Makes maintenance easier

- Reduces human error

Sorting is optional — you stay in control.

## Design Philosophy

This tool intentionally avoids:

- Over-engineering

- Heavy frameworks

- Cloud dependencies

- User accounts

Instead, it focuses on:

- Predictability

- Transparency

- Enterprise safety

- Zero side effects

Everything you copy is exactly what gets deployed.

## Try the Tool

You can access the Edge Managed Favorites Builder here:

**[https://using-it.dk/EdgeBookmarsCreator/](https://using-it.dk/EdgeBookmarsCreator/)**

If you manage Edge via Intune or work with cross-platform endpoint management, this tool should save you both time and frustration.