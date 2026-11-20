---
title: "Conditional Access: A Persona-Based Framework for Scalable Access Control"
description: ""
pubDate: "2025-11-14 13:15:34"
updatedDate: "2025-11-23 17:09:31"
slug: "conditional-access-a-persona-based-framework-for-scalable-access-control"
draft: false
categories:
  - "conditionalaccess"
tags: []
wordpress_id: "378"
original_url: "https://using-it.dk/conditional-access-a-persona-based-framework-for-scalable-access-control/"
---

Conditional Access is not just another security feature in Microsoft’s portfolio – it’s a cornerstone of any modern Zero Trust strategy. But deploying it effectively requires more than technical know-how. It demands a structured, strategic approach that balances security, user experience, and scalability.

This article outlines a practical, persona-based framework I use when implementing Microsoft Entra Conditional Access with clients. The goal is to create a clear, maintainable, and future-proof access model that minimizes risk without compromising productivity.

<figure class="wp-block-image size-full is-resized">![](https://using-it.dk/wp-content/uploads/2025/11/image.png)</figure>

### Step 1: Start with a Global Deny-by-Default Policy

Many organizations begin Conditional Access implementation by protecting specific applications or roles. While understandable, this can leave gaps. Instead, reverse the logic: **protect everything by default**, and explicitly allow access based on known, trusted conditions.

I recommend starting with a global policy that blocks all access not explicitly allowed through defined persona-based policies. This ensures:

- New users and apps don’t gain unintended access

- Policies cover both known and unknown risks

- Accidental exclusions are prevented

> 
**Key Principle:** Every identity must be covered by at least one Conditional Access policy.

</blockquote>

### Step 2: Define Personas Based on Risk and Access Needs

Personas are logical groupings of users based on behavior, risk profile, and access requirements – not just job titles or departments. This abstraction simplifies policy design and ensures consistency across the organization.

Common personas include:

<figure class="wp-block-table"><table class="has-fixed-layout"><thead><tr><th>**Persona**</th><th>**Description**</th><th>**Typical Controls**</th></tr></thead><tbody><tr><td>**Admins**</td><td>Users with elevated privileges</td><td>Phishing-resistant MFA, compliant device, 8-hour session</td></tr><tr><td>**Internal Users**</td><td>Standard employees within the organization</td><td>MFA and/or device compliance, 7-day session</td></tr><tr><td>**Guests &amp; Externals**</td><td>Users outside the organization (partners, B2B collaborators)</td><td>Terms of Use, limited access, session control, 24-hour session</td></tr><tr><td>**Service Accounts**</td><td>Non-human accounts for automation or backend processes</td><td>Restrict by location/risk (MFA not supported)</td></tr><tr><td>**Workload Identities**</td><td>App identities or service principals</td><td>Restrict by location/risk, conditional access app controls</td></tr><tr><td>**Global**</td><td>Catch-all for any identity not explicitly mapped to a persona</td><td>Deny access or apply strictest controls</td></tr></tbody></table></figure>

By anchoring policy design to personas, you enable scalable access management that can evolve with your organization.

### Step 3: Layer Your Policies for Flexibility and Clarity

Instead of building monolithic policies, break them down into **modular policy types**, each focused on a specific control objective. This allows for easier management and clearer auditing.

<figure class="wp-block-table"><table class="has-fixed-layout"><thead><tr><th>**Policy Type**</th><th>**Purpose**</th></tr></thead><tbody><tr><td>**BaseProtection**</td><td>Core access policy per persona</td></tr><tr><td>**IdentityProtection**</td><td>Protect against compromise (e.g., block legacy auth, trigger MFA on risk)</td></tr><tr><td>**DataProtection**</td><td>Secure sensitive data with session controls, app restrictions, etc.</td></tr><tr><td>**AppProtection**</td><td>Apply special handling for high-risk or sensitive applications</td></tr><tr><td>**AttackSurfaceReduction**</td><td>Block access from unknown platforms, risky locations, or threat indicators</td></tr></tbody></table></figure>

> 
**Example:** A policy stack for Admins might include BaseProtection, IdentityProtection, and AttackSurfaceReduction.

</blockquote>

This layered approach provides depth in defense while maintaining flexibility.

### Step 4: Implement a Consistent Naming and Numbering Standard

To maintain transparency and scale effectively, every policy should follow a consistent naming and numbering scheme based on persona and policy type.

<figure class="wp-block-table"><table class="has-fixed-layout"><thead><tr><th>**Persona Group**</th><th>**CA Number Range**</th></tr></thead><tbody><tr><td>Global</td><td>CA000 – CA099</td></tr><tr><td>Admins</td><td>CA100 – CA199</td></tr><tr><td>Internal Users</td><td>CA200 – CA299</td></tr><tr><td>External Users</td><td>CA300 – CA399</td></tr><tr><td>Guest Users</td><td>CA400 – CA499</td></tr><tr><td>Service Accounts</td><td>CA500 – CA599</td></tr><tr><td>Workload Identities</td><td>CA600 – CA699</td></tr></tbody></table></figure>

<hr class="wp-block-separator has-alpha-channel-opacity is-style-wide"/>

**Example policy name:**

**CA101-AllKnownPersona-BaseProtection-AllApps-AnyPlatform-MFA**

Purpose: Enforce MFA for all users across all cloud apps except emergency break-glass.

### CA102-AllKnownPersona-BaseProtection-AllApps-AnyPlatform-BlockLegacyAuth

Purpose: Block legacy authentication globally.

### CA103-AllKnownPersona-BaseProtection-AllApps-CompliantOrMDfE-MFA

Purpose: Require compliant device or MDE risk level “Low”.

This format ensures quick readability and simplifies collaboration across IT and security teams.

### Step 5: Monitor, Evaluate, and Adjust

Implementation is just the beginning. Conditional Access policies must be actively monitored and adjusted as the environment changes.

Recommended practices include:

- Regular review of **sign-in logs** in Microsoft Entra

- Use of **dashboards or Entra Workbooks** for visual policy impact analysis

- Adjust policies based on **behavioral trends** and **threat intelligence**

This continuous feedback loop ensures the framework stays effective over time.

### Final Thoughts: It’s a Framework, Not a One-Off

Conditional Access is not just about controlling logins – it’s about building a **transparent, scalable identity control strategy** that aligns with Zero Trust principles.

By:

- Starting with a deny-by-default mindset

- Defining access through personas

- Applying layered, modular policies

…you create a secure, structured, and sustainable access control platform.

This is my recommended framework, but there’s no one-size-fits-all. What matters most is that your Conditional Access design is **structured, intentional, and tailored to your organization’s reality**.