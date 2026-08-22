# EIB GitHub Access and Verification

**Created:** 2026-08-22  
**Status:** Active Operational Guidance  
**Repository:** `bjohnson70/EIB`  
**Authoritative Branch:** `main`

---

## Purpose

This document records the approved method for validating ChatGPT access to the EIB GitHub repository.

It exists because an August 2026 troubleshooting session demonstrated that GitHub repository-discovery and GitHub App installation enumeration can return no repositories even while direct access to the public EIB repository remains fully functional.

The resulting lesson is:

> **Failure to enumerate repositories does not prove failure to access a known repository.**

For a known EIB repository, direct repository and file access must be tested before changing authentication, OAuth, GitHub App, or repository permissions.

---

# 1 — Known EIB Repository

The authoritative public EIB repository is:

`bjohnson70/EIB`

The authoritative operational branch is:

`main`

When validating EIB access, use these values directly rather than attempting to rediscover the repository first.

---

# 2 — Primary Access Test

The first GitHub access test should be a direct request against:

`bjohnson70/EIB`

The test should verify that repository metadata can be read.

Expected results should include:

- Repository name: `EIB`
- Owner: `bjohnson70`
- Visibility: Public
- Default branch: `main`

Successful direct access establishes that the repository itself is reachable.

---

# 3 — Branch Verification

After repository access succeeds, explicitly verify the authoritative branch:

`main`

Do not assume that successful repository authentication proves that the intended branch is being read.

Repository configuration, directories, requirements, and implementation files should normally be validated against `main` unless a development task explicitly identifies another branch.

---

# 4 — Content Verification

After the repository and branch are confirmed, perform a direct content request.

Recommended initial tests include:

- Repository root
- Known directory
- Known file

For example:

`bjohnson70/EIB`

↓

`main`

↓

Repository root

↓

`DEVELOPMENT/`

↓

Known Markdown file

A successful file or directory read proves usable repository access more reliably than repository enumeration alone.

---

# 5 — Do Not Use Repository Enumeration as the Primary Test

The following mechanisms may be useful for repository discovery:

- Repository listing
- Installation listing
- Installed-account listing
- GitHub App repository enumeration
- Search of installed repositories

However, they must **not** be treated as the authoritative access test for a known public EIB repository.

During the August 2026 troubleshooting session, these mechanisms returned:

> **0 repositories / 0 installations**

This initially appeared to indicate that ChatGPT could not access EIB.

That conclusion was incorrect.

A subsequent direct GitHub request to:

`bjohnson70/EIB`

successfully returned the repository, its metadata, the `main` branch, and repository contents.

---

# 6 — Correct Interpretation of Zero Enumeration Results

If repository or installation enumeration returns zero results:

Do **not** immediately conclude:

> ChatGPT cannot access GitHub.

Do **not** immediately conclude:

> ChatGPT cannot access EIB.

Do **not** immediately:

- Revoke OAuth authorization
- Disconnect GitHub
- Reinstall integrations
- Change repository visibility
- Change repository permissions
- Change branch configuration
- Modify the EIB repository

Instead:

> **Attempt direct repository access first.**

---

# 7 — Troubleshooting Sequence

When GitHub access is questioned, use the following sequence.

## Step 1 — Identify the Known Repository

Use:

`bjohnson70/EIB`

## Step 2 — Directly Fetch Repository Metadata

Confirm that EIB can be read.

## Step 3 — Confirm Branch

Verify:

`main`

## Step 4 — Read Repository Root

Confirm actual directory/file visibility.

## Step 5 — Read a Known Directory

Examples may include:

- `DEVELOPMENT/`
- `ARCHITECTURE/`
- `CONFIG/`
- `DOCUMENTATION/`
- `IMPLEMENTATION/`

## Step 6 — Read a Known File

Confirm actual file content can be retrieved.

## Step 7 — Only Then Troubleshoot Authentication

If direct repository or content access fails, investigate:

- ChatGPT GitHub connection
- GitHub authorization
- GitHub App installation
- Repository permissions
- Account mismatch
- Repository visibility
- Branch/reference errors

---

# 8 — Public Repository Consideration

EIB is a public GitHub repository.

A public repository may be directly readable even when a GitHub App installation or repository enumeration mechanism does not expose it through an installed-repository list.

Therefore:

> **Public repository readability and GitHub App installation enumeration are separate tests.**

Do not confuse one with the other.

---

# 9 — Read Access Versus Write Access

Successful direct repository access proves that ChatGPT can read the repository through the available GitHub interface.

It does not automatically prove that every GitHub write operation is available or authorized.

Read and write capability should be tested separately when required.

Examples of write capability include:

- Creating files
- Updating files
- Creating branches
- Creating issues
- Creating pull requests
- Committing changes

Do not represent read access as proof of write access.

---

# 10 — Evidence-Based Verification

When asked:

> **Can you access EIB?**

The preferred verification is not simply an authentication check.

Verify actual repository content.

A strong response should be based on successful retrieval of:

1. Repository metadata
2. `main` branch
3. Repository directory
4. File or directory contents

This demonstrates functional access rather than merely credential presence.

---

# 11 — August 2026 Operational Lesson

During development of EIB v8 requirements, one ChatGPT session appeared unable to access the EIB repository while another EIB GitHub Setup session had successfully read and reported repository directories and files.

Troubleshooting initially focused on:

- GitHub account authorization
- ChatGPT GitHub permissions
- GitHub OAuth authorization
- GitHub App installation
- Installed repository enumeration

The critical discovery was that the failing session had been using repository/installation enumeration as its primary verification mechanism.

Once the session directly requested:

`bjohnson70/EIB`

the repository was successfully returned.

Direct access also confirmed:

- Repository: `bjohnson70/EIB`
- Visibility: Public
- Default branch: `main`
- Repository contents were readable

The apparent access failure was therefore primarily a **verification-method failure**, not an EIB repository failure.

---

# 12 — Operating Rule for Future ChatGPT Sessions

For EIB repository work:

> **Known repository first. Discovery second.**

When the repository is already known, ChatGPT should directly reference:

`bjohnson70/EIB`

and explicitly use:

`main`

when branch certainty is required.

Repository discovery should be used when the repository itself is unknown, not as a mandatory prerequisite for accessing a known repository.

---

# 13 — Verification Standard

EIB GitHub access may be considered verified when:

- [ ] `bjohnson70/EIB` can be directly retrieved
- [ ] Repository metadata is readable
- [ ] `main` is confirmed
- [ ] Repository root is readable
- [ ] At least one known directory is readable
- [ ] At least one known file can be retrieved

If these tests succeed:

> **EIB read access is operational.**

Separate testing is required before asserting write capability.

---

# Final Principle

> **Test the capability you actually need.**

If the task requires reading a known EIB file, test reading that file.

Do not allow a failure in an unrelated repository-discovery mechanism to override successful direct evidence that the repository and its contents are accessible.