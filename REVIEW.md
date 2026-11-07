# reboc.nl: positioning review

Date: 7 November 2026
Reviewed by: Claude Code, at Reinier's request
Status: **review only, no files changed**

---

## 1. Source, hosting and deployment

| Item | Finding |
| --- | --- |
| Source | This repository, `~/Projects/reboc-web`. Four static HTML pages, no build step, all CSS inline per page. |
| Repository | `github.com/sailingshaman/reboc-web`, branch `main` |
| Hosting | Cloudflare, connected to the GitHub repository. A push to `main` deploys automatically (confirmed in practice on 11 October 2026). |
| Live URL | https://reboc.nl. Note that `/terms-conditions.html` serves a 307 redirect to `/terms-conditions`. |
| Current branch | `claude/reboc-unique-design-d4fcff`. Design work on this branch is parked; this review assumes the existing design stays. |

No open question here, so nothing to ask.

---

## 2. Two things to flag before anything else

**a. This brief reverses two recent, deliberate changes.**

- Commit `5eaccf4`, "Reword site to reflect purely administrative intermediary role", moved the site **towards** the wording this brief now rules out.
- Terms and Conditions version 2.0 (commit `ca257db`, pushed live 11 October 2026) added the phrase "an intermediary agreement (intermediairsovereenkomst)" to article 1.3.

Both were correct for the model as it was described at the time. If the positioning has genuinely changed, that is fine, but please confirm it explicitly, because the live Terms are referenced in your agreements with specialists and a second reversal within a month is itself a signal.

**b. The two policy PDFs carry the same problem as the HTML, and they have already been sent out.**

`Reboc_BV_Human_Rights_Policy.pdf` and `Reboc_BV_Human_Rights_Risk_Analysis_Process.pdf` both contain "IT staffing intermediary" and "recruitment, placement". These were produced for the Dell supplier assessment. Changing the HTML without regenerating the PDFs leaves a visible mismatch between your website and a document a client already holds. See section 6.

---

## 3. index.html

### 3.1 Head and metadata

| Loc | Current | Why it is a problem | Proposed |
| --- | --- | --- | --- |
| `index.html:6` | `<title>Reboc B.V. \| IT Staffing & Project Services \| Den Haag</title>` | "IT Staffing" in the single most visible tag. Appears in search results and browser tabs. | `Reboc B.V. \| IT Project Delivery by Independent Specialists \| Den Haag` |
| `index.html:7` | meta description: "administrative partner ... We handle contracting, invoicing, and compliance. Freelancers in our network cover ..." | "network" and "administrative partner" frame Reboc as a pool plus admin, not a contracting subcontractor. | "Reboc B.V. delivers IT services to professional services organisations as a subcontractor, through independent senior specialists working to defined deliverables with acceptance. Based in The Hague." |
| `index.html:8` | `<meta name="keywords">` with 60+ terms | Contains: IT staffing Netherlands, IT intermediary, IT recruitment Netherlands, detachering ICT, IT secondment Netherlands, IT staffing agency Holland, factoring IT, factoring ZZP, factoring freelancers, factoringmaatschappij ICT, invoice factoring freelancers, freelancer payroll services, payrolling IT, verloningspartij ICT, bemiddeling ZZP, freelancer mediation, IT workforce solutions, freelance developer placement, wet DBA compliant, DBA compliance, schijnzelfstandigheid, modelovereenkomst, tussenkomst, ZZP inhuur. Every one of these contradicts the model, and "wet DBA compliant" is a claim you should not make. | **Delete the tag entirely.** Google has ignored meta keywords since 2009. There is no SEO cost and it removes 24 contradicting terms in one edit. |
| `index.html:16` | `og:title` "IT Staffing & Project Services" | Same as title. This is what LinkedIn renders when the link is shared. | Match the new title |
| `index.html:23` | `twitter:title` idem | Same | Match the new title |
| `index.html:39` | JSON-LD `description`: "Administrative intermediary for independent IT freelancers and enterprises" | Structured data is read by compliance tooling and by Google. "Administrative intermediary" is the exact framing to drop. | "Subcontractor delivering IT services to professional services organisations through independent specialists, on defined deliverables with acceptance by the client." |
| `index.html:47` | `"foundingDate": "2009"` | Contradicts the About section, which says 2004, and the "20+ years" claim. One of the three is wrong. | Open question Q1 |
| `index.html:50-55` | `serviceType` array | Lists four disciplines. Needs confirming, see Q3. | Pending Q3 |

### 3.2 Visible copy

| Loc | Current | Why it is a problem | Proposed |
| --- | --- | --- | --- |
| `index.html:1002` | Hero badge: "Beyond IT Transformation" | Means nothing, and reads as filler. | Remove, or replace with "Den Haag, since [year]" |
| `index.html:1003` | H1: "Skilled **IT Freelancers** for Ambitious Enterprises" | Offers people, not results. Reads as a supply of workers. | "Defined results, delivered by senior IT specialists" |
| `index.html:1004` | "Reboc B.V. is the administrative partner for independent IT freelancers and the enterprises they work with. We take care of contracting, invoicing, and compliance so both sides can focus on what matters" | "administrative partner ... for both sides" is the matchmaker framing. Also "compliance" as something Reboc takes care of for others. | See draft copy in section 7 |
| `index.html:1034` | "Independent freelancers **in our network** cover four key disciplines." | "our network" implies a pool of available people. | "Reboc delivers assignments in four areas." |
| `index.html:1073` | "A simple process to get the administration sorted, so the freelancer can get to work." | Reduces Reboc to admin. | See draft copy, section 7 |
| `index.html:1077-1080` | Step 1 "Introduction": "A freelancer and a client find each other. We step in to handle the administrative side" | **The single most damaging sentence on the site.** This is textbook bemiddeling: the parties find each other, Reboc does the paperwork. | Rewrite to: the client defines an assignment, Reboc contracts both sides |
| `index.html:1082-1084` | Step 2 "Contracting": "We set up the agreements **between** freelancer and client" | States that Reboc is not a party to the agreements. The opposite of the model. | "Reboc contracts the specialist's company, and contracts the client separately, back to back. Reboc is the contracting party on both sides." |
| `index.html:1116` | "Quick turnaround on **placements** and payments" | "placements" | "Contracts, invoices and acceptance records are handled promptly" |
| `index.html:1124-1126` | "**Fully Compliant.** Dutch labour law, tax regulations, insurance: we stay on top of it all so you don't have to worry." | Overpromise and a liability transfer in the wrong direction. Tells specialists they need not worry about their own tax position, which is exactly what an inspector would quote back at you. | Replace the whole card with a factual "How engagements are structured" item. Draft in section 7. |
| `index.html:1143` | "Established in 2004, we've built deep expertise in **IT staffing and freelancer management**" | "staffing", and "freelancer management" implies direction over people. | "Reboc has delivered IT assignments from The Hague since [year]." |
| `index.html:1190` | "We are a **purely administrative intermediary**: we handle contracting, invoicing, and compliance for independent IT freelancers and their clients." | The exact phrase the brief rules out. | "Reboc is a subcontractor. We contract the specialist's company and the client separately, deliver the agreed services, and handle the administration that goes with it. We do not direct how the work is done." |
| `index.html:1188` | About H3 "Your administrative partner in IT" | Same framing. | "A subcontractor delivering defined results" |

---

## 4. terms-conditions.html (LEGAL, for lawyer review)

These are referenced in your agreements with specialists. Every change below needs your lawyer.

| Loc | Current | Why | Proposed |
| --- | --- | --- | --- |
| `:7` | meta description "Reboc B.V. IT staffing and project services" | "staffing" | Match new positioning |
| `:290` (art 1.3) | "such as an intermediary agreement (**intermediairsovereenkomst**) or a statement of work" | Added by me on 11 October and now live. "Intermediairsovereenkomst" names Reboc as intermediary in a document your specialists sign. | "such as a services agreement (dienstverleningsovereenkomst) or a statement of work" |
| `:298` (art 2) | "**Services** -Intermediary, facilitation, invoicing, and administrative services offered by Reboc." | Defines Reboc's own services as intermediary and facilitation. | "Services: IT services delivered by Reboc through independent specialists, together with the contracting, invoicing and administration that supports them." |
| `:304` (art 3.1) | "Reboc provides professional **intermediary** services by **connecting** Clients with Customers and facilitating invoicing" | Core definition of the business as connecting parties. | "Reboc contracts with Customers to deliver defined IT services, and contracts separately with Clients to perform those services. Reboc is the contracting party in both relationships." |
| `:325` (art 6.3) | "deduct any agreed fees or **commissions** prior to remittance" | "commission" is the compensation model of a bemiddelaar. Reboc resells at its own rate. | "Reboc pays the Client the rate agreed in the written agreement with that Client. The difference between the Client rate and the Customer rate is Reboc's own margin on the services it sells." |
| `:327` (art 6.5) | "The fees, **commissions** and rates applicable to a Client" | Added by me on 11 October, now live. Same issue. | "The rates applicable to a Client are exclusively those specified in the written agreement between Reboc and that Client." |
| `:332` (art 7.1) | "Reboc does not guarantee any outcome, such as **placement**, contract execution" | "placement" | "such as the award of an assignment, contract execution, or payment by Customers" |
| `:281` | "Version 2.0 &mdash; 11 October 2026" | Em dash, which your constraints exclude. My own change, my error. | "Version 2.1, [date]" |
| Structural | Articles 2 and 9 use `<ul>`, so article 9.3 has no visible number | You cite these articles in agreements. An unnumbered clause is hard to reference. | Convert both to `<ol>` |

Also worth considering, and a question for your lawyer rather than a finding: the Terms are written as website terms for "visitors, clients and users", yet they are referenced in commercial agreements. Those are two different documents doing one job.

---

## 5. privacy-notice.html (LEGAL, for lawyer review)

| Loc | Current | Why | Proposed |
| --- | --- | --- | --- |
| `:281` | "Reboc B.V. is an **IT intermediary company** ... We **connect** freelance IT professionals with enterprise clients and handle the related administration and invoicing." | Same framing as the homepage. | "Reboc B.V. delivers IT services to its clients through independent specialists, each contracted through their own company." |
| `:305` | Purpose: "To set up and manage contracts **between** freelancers and clients" | Repeats that Reboc is not a party. | "To contract with specialists and with clients, and to manage those contracts" |
| `:321` | Sharing: "The other party in a **freelancer-client engagement**" | Same | "Our client, limited to what is necessary for the assignment" |

**Additions the brief requires** (currently absent entirely):

- Categories: work logs, deliverable and acceptance records, quarterly check-in answers, evidence of independent working (KvK history, insurance, other clients, certifications).
- Purposes: demonstrating that assignments are performed independently; meeting obligations under Dutch law.
- Legal basis for the above (legitimate interest, and legal obligation where applicable).
- Retention per category, not only the two currently listed.
- Processors: add Hetzner Cloud **once the compliance application is live**, not before. Do not list a processor you are not yet using.
- A note that specialists can obtain a copy of their own evidence pack.

Two existing statements to verify rather than rewrite: "we do not use cookies, tracking pixels, or analytics tools" (`:293`) and the Formspree and Cloudflare processor list. Both looked accurate against the code, but confirm Formspree's current DPA.

---

## 6. human-rights-policy.html and the two PDFs (LEGAL, for lawyer review)

| Loc | Current | Why |
| --- | --- | --- |
| `:281` | "As an **IT staffing intermediary** connecting freelance professionals with enterprise clients" | Opening sentence of a document held by Dell |
| `:291` | "Decisions regarding hiring, **placement**, compensation, training, and termination" | Describes Reboc as making employment decisions about the specialists |
| `:304` | "While Reboc B.V. primarily facilitates **IT staffing** and project services" | "staffing" |
| `:318-320`, `:329-337` | 12 literal em dashes | Excluded by your constraints |

**The harder problem.** Sections 2, 5, 6 and 7 ("Freely chosen employment", "Fair wages and benefits", "Working hours", "Freedom of association") are written as if Reboc has workers: wages, overtime, one day off per seven, collective bargaining. For a company whose position is that it contracts independent companies, this reads as a description of an employer.

This is a genuine trade-off and I am not going to resolve it for you:

- These sections exist because Dell's supplier assessment asks for them. Removing them may fail the questionnaire.
- Keeping them undermines the position the rest of the site will take.

My suggestion is to keep the sections but scope each one explicitly, for example "Reboc contracts independent companies and does not employ the specialists who deliver its services. Where Reboc does employ staff, the following applies." Your lawyer should decide, with the Dell questionnaire in front of them.

**The PDFs.** Both contain the same wording and have already been supplied to Dell. If the HTML changes, the PDFs must be regenerated and, ideally, resupplied. I cannot regenerate them from this repository: there is no source document, only the PDFs. See Q6.

---

## 7. Proposed page structure and draft copy

> **Superseded on 7 November.** The copy below was the first draft and was published, then cut twice: once for length, once to remove assertions Reboc cannot evidence per assignment. Sentences here describing what the specialist or the client does are **no longer on the site**. See "Reductions after publication" at the end of this document for what the page says now.

Structure changes to index.html: keep the existing sections, rewrite three of them, and split "Why Reboc" into two audience blocks.

```
Hero
What we deliver        (was Services, four areas, pending Q3)
How it works           (rewritten, five steps instead of three)
For clients            (new, split from Why Reboc)
For specialists        (new, split from Why Reboc)
About                  (rewritten)
Contact                (unchanged)
```

### Hero

> **Defined results, delivered by senior IT specialists.**
>
> Reboc B.V. is a subcontractor to the professional services organisations of software vendors. We deliver IT services through independent specialists, each working through their own company, against deliverables with agreed acceptance criteria. We contract both sides and handle the administration.

### How it works

1. **Assignment defined.** The client sets out the assignment: scope, deliverables or backlog items, acceptance criteria, period and the country where the work takes place.
2. **Back to back contracts.** Reboc contracts the specialist's company under a standard agreement and a Statement of Work. Reboc contracts the client separately under the client's own order document. Reboc is the contracting party in both.
3. **Independent delivery.** The specialist decides how, when and with which means the work is done, using their own equipment, and remains free to work for other clients.
4. **Acceptance.** The client's project manager accepts the delivered work against the agreed criteria.
5. **Invoicing and payment.** Reboc invoices the client for accepted work. Reboc pays the specialist for accepted work after the client has paid.

### For clients

- **One contracting party.** Reboc carries the contract with you and the contract with the specialist's company.
- **Services, not people.** Assignments are defined as deliverables or backlog items with acceptance criteria, accepted by your project manager.
- **Documentation per assignment.** A Statement of Work, acceptance records and supporting evidence, available for your own supplier and compliance review. Reboc describes how engagements are set up; it does not give legal assurances about them.
- **Specialists who run their own business.** Own company, own professional liability insurance, own equipment, other clients.

### For specialists

**What we expect:** your own company (B.V., GmbH, Ltd), your own professional liability insurance, your own equipment, the freedom and the intention to work for other clients, and responsibility for your own tax and social security position.

**What we offer:** a standard agreement and a Statement of Work per assignment, deliverables and acceptance criteria agreed before you start, invoicing and administration handled, and a documented record of how you worked independently, which you can request for your own use.

**How payment works:** Reboc pays for work that the client's project manager has accepted, after the client has paid Reboc. This is stated in the Statement of Work.

### Replacement for the "Fully Compliant" card

> **How engagements are structured**
> Each assignment is set out in a Statement of Work with deliverables or backlog items and acceptance criteria. Reboc contracts the specialist's company and the client separately, back to back. The client's project manager accepts the work. Reboc does not direct how the work is done.

### About

> Reboc B.V. has delivered IT assignments from The Hague since [year, see Q1]. We work as a subcontractor to the professional services organisations of software vendors, delivering services through independent specialists who each work through their own company.
>
> We contract the specialist's company and the client separately, deliver the agreed services, and handle the contracting, invoicing and administration that go with them. We do not direct how the work is done; that is for the specialist, within the deliverables and acceptance criteria agreed with the client.
>
> Registered activities: SBI 62200 (computer consultancy) and SBI 82100 (administrative and support service activities).

---

## 8. Accessibility

I checked rather than assumed. Current state is better than expected.

| Check | Result |
| --- | --- |
| Headings | One `<h1>` per page, `<h2>` and `<h3>` in order. Pass. |
| Images and alt text | No `<img>` elements on any page. Not applicable. |
| Form labels | All four fields have `<label for>` matching the input `id`. Pass. |
| Mobile menu button | Has `aria-label="Toggle menu"`. Pass. |
| Text contrast | Measured all main pairs against WCAG AA 4.5:1. Lowest is the section subtitle grey at **4.76:1**. The cyan accent is 2.43:1 on white but is only ever used on the dark navy background, where it is 7.47:1. **No failures.** |
| Blinking element | `index.html:294-302`, the hero badge dot blinks indefinitely (`animation: blink 2s infinite`). WCAG 2.2.2 expects blinking to stop within five seconds. Minor, and the badge is proposed for removal anyway. |
| Language | `lang="en"` on all pages, correct for English content. |

One thing to fix if a Dutch version is added: Dutch passages inside an English page need `lang="nl"` on the element.

---

## 9. Housekeeping

- `sitemap.xml` gives `lastmod` 2026-03-28 for the Terms page, which changed on 11 October 2026. Update the dates when publishing.
- The live site redirects `/terms-conditions.html` to `/terms-conditions`, but `sitemap.xml` lists the `.html` URLs. Worth aligning so the sitemap lists the canonical URLs.
- The four pages each carry a full private copy of the CSS. Not a positioning issue, but any visual change has to be made four times. Extracting one shared stylesheet would make the eventual design change and the legal page styling consistent in one place.

---

## 10. Dutch version: recommendation

**My recommendation is not to build one yet, and to reconsider after the English rewrite is approved.**

Reasons: your clients are the professional services organisations of international vendors and their procurement and compliance teams work in English. Your specialists work through companies in several countries. A second language doubles the surface on which wording can drift out of step, and drift between two versions of the same claim is precisely the failure mode the rewrite exists to prevent.

The case for Dutch is a Belastingdienst or Nederlandse Arbeidsinspectie reader, who will read Dutch terms in Dutch. If that is the driver, a better answer than a full Dutch site is a single Dutch page stating the model in the Dutch legal vocabulary, maintained as one document. Say the word and I will propose it separately.

---

## 11. Open questions

These block the rewrite. I have not assumed answers.

| # | Question | Why it matters |
| --- | --- | --- |
| Q1 | **Founding year: 2004 or 2009?** About says 2004, the JSON-LD says 2009, the hero says "20+ years". | Three sources, two answers. A date a client can check against the KvK register. |
| Q2 | **Is the phone number +31 (0)70 569 0259 still correct?** | Changed in commit `fbad349`; please confirm it is current. |
| Q3 | **Are all four service areas still offered?** In particular Power BI and dashboarding, and software development (Go, Python, C#). | The brief flags these specifically. Listing work you no longer do is the same category of error as the SOW problems. |
| Q4 | **May clients be named?** The brief says do not name Broadcom, Dell or ING without your explicit approval. The draft copy above therefore says "professional services organisations of software vendors". | Naming them would make the positioning far more concrete. It is your call and your clients' contracts may restrict it. |
| Q5 | **Has the positioning genuinely changed since 5 October?** See section 2a. | Two reversals in a month, on a document your specialists sign. |
| Q6 | **Who regenerates the two policy PDFs, and should Dell be resupplied?** There is no source document in the repository, only the output PDFs. | A website that contradicts a document a client holds is worse than either on its own. |
| Q7 | **Confirm the Waadi deregistration date of 1 May 2026 and the current SBI codes**, so the About section can state them. | These are checkable facts and should be exactly right. |
| Q8 | **Does your lawyer want to see the Terms, Privacy Notice and Human Rights Policy together or separately?** | They interact: the Terms define the model, the Human Rights Policy currently contradicts it. |

---

## 12. What I propose to do next

1. You answer Q1 to Q8, or tell me to proceed with the questions marked in the copy as `[to confirm]`.
2. You approve or amend the draft copy in section 7.
3. I implement on a new branch cut from `main`, keeping the existing design and code style.
4. I show you the diff. **I do not deploy.** Given that a push to `main` goes live automatically, I will push to a branch only, and you merge when your lawyer has cleared the legal pages.

---

# Implementation log

Implemented 7 November 2026 on branch `claude/reboc-positioning-rewrite`, after Reinier answered the open questions. **Not deployed.**

## Answers received

| # | Answer | How it was applied |
| --- | --- | --- |
| Q1 | Sole proprietorship 2004, Reboc B.V. 2006 | Visible copy says "since 2004, as a sole proprietorship from 2004 and as Reboc B.V. since 2006". JSON-LD `foundingDate` corrected from 2009 to **2006**, since that element describes the legal entity. |
| Q2 | Phone correct | Unchanged |
| Q3 | Reboc does deliver the services; list the real areas | Four generic disciplines replaced by three. Power BI and software development removed. **The three areas are my proposal and need your confirmation.** |
| Q4 | Clients may be named, then reversed on 7 November | Initially named, then **removed from all six places** at Reinier's request. The copy now describes the client type, "the professional services organisations of enterprise software vendors". Reasons for removing: both vendors restrict partner use of their name without written consent; naming exactly two clients advertises concentration; the site would be wrong the moment a relationship ends; and naming clients contributes nothing to the positioning problem, which is about services rather than about anonymity. |
| Q5 | Not understood | Explained separately. Proceeded on the basis that the subcontractor description is the accurate one. |
| Q6 | PDFs may be rewritten | Both regenerated, see below. |
| Q7 | Waadi deregistration confirmed | Stated in the About section and in the Terms. |
| Q8 | Revise the legal pages as needed | Done, logged below. |

## Legal page changes, for the lawyer

### terms-conditions.html, now Version 2.1

| Article | Change |
| --- | --- |
| Meta description | "IT staffing and project services" replaced |
| 1.3 | "intermediary agreement (intermediairsovereenkomst)" becomes "services agreement (dienstverleningsovereenkomst)" |
| 2 | Changed from an unnumbered list to a numbered one. "Freelancer" becomes "Specialist". "Customer" redefined as a party contracting with Reboc rather than one "introduced via Reboc". "Services" redefined as the IT services Reboc contracts to deliver. |
| 3 | Rewritten and **extended from three clauses to four**, so former 3.2 is now 3.3 and former 3.3 is now 3.4. New 3.1 states Reboc contracts both sides and is responsible to the Customer for delivery. New 3.2 covers the Statement of Work and acceptance by the Customer's project manager. New 3.4 states Reboc invoices **in its own name**, replacing "on behalf of Clients and remit collected funds", which described a payment intermediary. |
| 6 | Rewritten. "Commissions" removed throughout. New 6.3 states the margin model explicitly and that no fee or commission is charged to a Client. |
| 7.1 | "placement" becomes "the award of an assignment" |
| 9 | Changed from an unnumbered list to a numbered one, so the indemnity added in version 2.0 is now visibly numbered 9.3 |
| Header | Em dash removed from the version line |

**The two denial clauses, resolved on 7 November.** Both originally kept their trigger words. Reinier chose to keep the legal substance while removing the words, so they now read:

- Article 3.3: "Reboc does not employ Clients and **does not supply personnel to work under the direction and supervision of a third party**." Direction and supervision by a third party is the substantive test under the Waadi, so the denial stands, without the statute being named.
- Article 6.3: "... is Reboc's own margin on the Services it sells. **Reboc charges the Client nothing for the engagement itself.**"

The Terms now contain none of the excluded words. Your lawyer may still prefer an express reference to the Waadi in article 3.3; that is a legal judgement, not a drafting one.

**Note on clause numbering.** Article 3 was renumbered because its content was rewritten. If any signed agreement cites article 3.2 or 3.3 of the Terms by number, that reference now points elsewhere. Worth checking before publishing.

### privacy-notice.html, now Version 2.0

- Section 1 no longer calls Reboc an "IT intermediary company"
- Section 2: added work logs, deliverables, acceptance and return records, periodic check-in answers, and evidence of independent working
- Section 3: purposes extended to cover acceptance, payment and the record of how assignments are carried out
- Section 4: added a legitimate-interest basis for keeping those records
- Section 5: "the other party in a freelancer-client engagement" becomes "our client"
- Section 7: retention periods added per new category, plus a line stating a specialist may request a copy of their own records

**Not added: Hetzner.** The compliance application is not live, so listing it as a processor would be inaccurate today. It must be added before the Hetzner front door processes any personal data. The data processing agreement and the privacy statement for specialists are yours to arrange, not code tasks.

### human-rights-policy.html, now Version 2.0

- Section 1 no longer calls Reboc an "IT staffing intermediary"
- Section 1 has a **new Scope paragraph** stating that Reboc does not employ the specialists, and that references to workers, wages, working hours and employment apply to Reboc's own personnel and otherwise express the standards expected of contracted companies and partners. This is my answer to the trade-off in section 6 of the review: it keeps the sections Dell's questionnaire expects, while removing the implication that Reboc employs the specialists. **Please have this checked against the Dell supplier assessment.**
- Section 4: "hiring, placement, compensation, training, and termination" rewritten
- Section 8: "primarily facilitates IT staffing and project services" rewritten
- 12 em dashes replaced with colons
- Section numbering unchanged, so the internal cross-reference in section 14 to "Section 3" still resolves

### The two PDFs

Both regenerated and now free of the contradicting wording.

- `Reboc_BV_Human_Rights_Policy.pdf`, 5 pages, now **generated from `human-rights-policy.html`**, so the page and the PDF cannot drift apart again.
- `Reboc_BV_Human_Rights_Risk_Analysis_Process.pdf`, 3 pages, rewritten from the extracted text of the old PDF. Its scope section now states that Reboc does not employ the specialists. Risk areas reworded: "Labour rights ... for freelancers placed at client sites" becomes "Contract terms and fair dealing"; "recruitment, placement" becomes "engagement and the continuation of assignments".
- New folder `docs-source/` holds the source and `build.py`. Run `python3 docs-source/build.py` from the repository root to regenerate both. This answers Q6: there is now a source document.

**Dell already holds the old versions.** Resupplying them is your call.

## Non-legal changes

- `index.html`: meta keywords tag deleted outright (24 contradicting terms removed in one edit, no SEO cost). Title, description, Open Graph, Twitter and both JSON-LD blocks rewritten. Hero, services, process, audience and about sections rewritten. Process went from three steps to five; the step grid changed from a fixed three columns to `auto-fit` to carry them.
- Two new CSS rules for the "For clients" and "For specialists" group headings, using the existing variables.
- `sitemap.xml`: all four `lastmod` dates set to 2026-11-07.
- `.gitignore` added for `.claude/` and the generated build artefact.

## Verification performed

| Check | Result |
| --- | --- |
| Forbidden-term sweep, all four pages | Clean, except the two deliberate negations in the Terms and "European Commission" in the privacy notice |
| Em dashes, all four pages and both PDFs | Zero |
| HTML tag balance, all four pages | Valid |
| Internal cross-references | Intact |
| Rendering at 1280px and 980px | Checked in a browser |
| PDFs | Regenerated, read back, 0 contradicting terms |

## Still open

1. **Confirm the three service areas.** My proposal: VMware Cloud Foundation platform delivery, enterprise cloud and virtualisation migration, project leadership for infrastructure programmes.
1a. ~~One sentence still names the Waadi.~~ **Resolved 7 November: removed.** The About section previously read "Reboc is not registered as a provider of temporary labour and withdrew its Waadi registration with effect from 1 May 2026." It was cut, because Waadi registration is declaratory rather than constitutive, so the sentence proved nothing about Reboc's position, while stating on the public record that Reboc **was** registered as making workers available until 1 May 2026, a period that overlaps the window any back-assessment would cover. The deregistration date also reads as a response to tightening enforcement. The substance is preserved without the history, in Terms article 3.3 and in the About line "We do not direct how the work is done". Only the SBI codes remain. **If a client questionnaire asks directly about Waadi registration, it must still be answered fully, including the history. Discuss the 2025 to 2026 exposure with your lawyer.**
2. **Lawyer review** of the three legal pages and both PDFs.
3. **Check whether any signed agreement cites Terms article 3.2 or 3.3 by number.**
4. **Decide on resupplying the PDFs to Dell.**
5. The homepage still carries the generic visual design. The three alternatives from the earlier design review are parked on branch `claude/reboc-unique-design-d4fcff`.

---

# Reductions after publication

The copy in section 7 went live on 7 November and was then reduced twice the same day, after Reinier raised two objections: the explanations were too detailed, and detail of that kind can be used against him.

## The test applied

Not "is this too long" but: **can Reboc evidence this today, for every assignment?** Statements about the contracting structure follow from documents Reboc holds. Statements about how the specialist or the client behaves do not, and the compliance application that would evidence them does not exist yet. A website that describes the intended practice sets a public benchmark that Reboc can be measured against under the Deliveroo factors.

One of the published sentences, "deliverables and acceptance criteria agreed before the assignment begins", was directly contradicted by Reboc's own document review, which found expired statements of work and a generic template used on unrelated work.

## Removed from the site

| Claim | Why |
| --- | --- |
| "The specialist decides how, when and with which means the work is done" | Describes the specialist's conduct |
| "The client's project manager accepts the work against the agreed criteria" | Describes the client's conduct |
| "Deliverables and acceptance criteria agreed before the assignment begins" | Contradicted by the document review |
| "Own company, own insurance, own equipment, other clients" as a statement about specialists | Asserts facts about third parties that Reboc does not verify. The same points remain on the specialist side, where they are stated as what Reboc expects |
| "Each assignment has its own Statement of Work" and "it is stated in every Statement of Work" | Universal claims about documents and their contents |
| "with acceptance by the client" in the meta description, Open Graph, Twitter and JSON-LD | The same claim, left in the head after the visible copy was cut. More exposed than body copy, since the meta description appears in search results and JSON-LD is machine readable |

Process reduced from five steps to three, all describing Reboc's own acts. Audience cards reduced from eight to six. The About stat tiles removed, with the SBI codes dropped from the page. Homepage copy from 737 words to 469.

## What the site now asserts

Every remaining statement follows from Reboc's own contracts or describes Reboc's own conduct:

- Reboc is a subcontractor, delivering through independent specialists who each work through their own company
- Reboc contracts the specialist's company and the client separately and is a party to both
- Reboc invoices the client and pays the specialist once the client has paid
- Reboc does not direct how the work is done, and does not supply people to work under the client's direction
- What Reboc expects of a specialist, stated as a requirement rather than as fact
- "We describe how we contract; we do not give legal assurances"

## Privacy notice trimmed on the same principle

The version published on 7 November listed work logs, acceptance and return records, periodic check-in answers, and an intake file of other clients, own equipment and certifications. Those belong to the compliance application, which is not live. Listing data Reboc does not yet process is the same error as naming a processor before it is used, which this review refused to do for Hetzner, and it would invite a request for records that do not exist.

Section 2 now lists only contact details, professional information, company and billing information, records of hours and invoiced work, and Chamber of Commerce and insurance details. The matching purpose, legal basis and retention lines were removed with them.

**Confirm this against what `reboc-adminster` actually holds.** I trimmed to what the system plausibly stores today, but only you can confirm it. Under-describing processing is a transparency failure under the GDPR, so this needs to be right in both directions. Add the removed categories back when the compliance application goes live, together with Hetzner as a processor.

## Still open after these reductions

1. The three service areas remain my proposal, not your confirmation.
2. Terms article 3.2 still states that scope is set out in a Statement of Work and that work is accepted by the Customer's project manager. I recommend keeping it: a contract should define the mechanism, and without it there is no contractual basis for "services, not people". But it is the same sentence pattern that was cut from the website, so your lawyer should confirm it.
3. Legal review of all three legal pages and both PDFs.
4. Whether to resupply the regenerated PDFs to Dell.
