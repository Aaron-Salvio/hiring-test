# SiteHost Challenge - Submission Introduction

Firstly, thank you for the opportunity to take part in this challenge. Below are my completed solutions for both Part 1 and Part 2.

---

## Part 1: API Integration

In Part 1, I created a script to interact with the provided API and retrieve a list of domains along with their associated DNS records for the client Business Systems International (client_id: 100).

I used Python for this task, and the script is saved as `fetch_dns.py`. It makes API calls to:
- `/domains/100` to get the list of domains and their DNS zones.
- `/zones/{zone_id}` to get DNS records for each zone.

The script prints out the domain names, DNS zones, and DNS records to the console in a readable format.

---

## Part 2: Resolving a Customer Issue

In Part 2, I investigated the issue described by Alice, who reported that the domain `site.recruitment.shq.nz` was completely inaccessible. The site was hosted on IP address `120.138.30.179`.

When visiting the domain in a browser, I encountered a secure connection error due to an invalid or missing SSL certificate.

To work around this, I visited the server directly using HTTP (not HTTPS) at `http://120.138.30.179`, which allowed me to load the site. Once there, I viewed the page source and found the required hidden code:

<!-- This is what you're looking for: SHF1ZzYwcVJDdVFVb3hFOVFBc2FaU3lVZjhnRFpoYXZPOWt5clRVY1dBPT0= -->


---

## Summary of Findings

The issue is due to a misconfigured or missing SSL certificate on the server. To fix this, Alice (or her team) needs to:
1. Ensure there is a valid SSL certificate for `site.recruitment.shq.nz`.
2. Configure the server to serve HTTPS traffic correctly on port 443.
3. Restart the web server once everything is set up.

I’ve explained all of this in `reply.md` in clear terms for Alice to understand and take action.

---

## Files Included

- `fetch_dns.py` – Python script for API Integration (Part 1)
- `reply.md` – My response to Alice, explaining the problem and how to fix it
- `README.md` – This file

---

Thank you again for reviewing my submission! Please feel free to reach out with any questions or feedback.
