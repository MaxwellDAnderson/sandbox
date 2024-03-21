# Proposed Extensions to Schema.org for Legal Documents

## Introduction

Several issues have been opened making suggestions for extending Schema.org to accommodate the description, markup, and annotation, of legal documents (_see_ list of related issues in the "References" section below). Some of these suggestions, such as `Legislation`, have been adopted and implemented. But many have not. That should change.

This proposal seeks to further extend Schema.org in a manner that makes its use more conducive to those in the legal profession. 



## Proposed New Classes

### `LegalDocument` (subclass of `CreativeWork`)

Description: A basic document holding legal significance that may not fit within any of the other more specific types of LegalDocument, including a pleading, court filing, memorandum, opinion letter, hearing transcript, deposition, etc.

### `CommunicationDocument` (subclass of `CreativeWork`)

Most useful inherited properties from `Thing`:

## New Properties for `CreativeWork`


### `marginNote`

* Expected Type: `Text`
* Description: A note that appears in the margin of the page alongside the main content. Used in a variety of academic and government texts.

### `printedPage`

* Expected Type: `Text`
* Description: Indicates the starting point for a printed page. This helps ensure the original pagination of a `CreativeWork` can be maintained if and when the `CreativeWork` is reproduced into another format (_e.g._, HTML) or is reprinted. 

### `starPage`

**Expected Type:** `Text`

**Description:** A special kind of page marker used to refer to the starting point of a page in an earlier printing or edition of a work that is distinct from the page as printed in the current edition/printing of the work. Often used for reprints of historically significant legal texts.

**Rationale:** Many legal texts seek to inform the reader of the original pagination of a reproduced or reprinted work. (An example of a star page is found in [this edition](https://www.google.com/books/edition/Commentaries_on_the_Laws_of_England/vKULAQAAIAAJ?hl=en&gbpv=1&pg=PA3&printsec=3) of Blackstone's Commentaries on the Laws of England. The link is to page 3, but look a little less than half-way down the page on the right margin, you will see a "\[*7\]". That is the star page.) This ensures that citation can still be made to the original an earlier printing or edition of the work. Similarly, where a `LegalDocument` is reproduced in multiple sources, each with different pagination, many commercial databases compile all of the different citations into one document so the user can cite to the source to which they may be legally obligated to cite. This can result in multiple instances of star pages, each with one additional star added before the page number. Thus, cited material appearing on page 130 of source one, page 150 of source two, and page 170 of source three would be indicated \[\*130\], \[\*\*150\], and \[\*\*\*170\], respectively.

## New Properties for `Article`, `Chapter`, `PublicationIssue`, and `PublicationVolume`

### Observations Regarding the Insufficiency of the `pageStart` and `pageEnd` Properties for Legal Citations

Citation to authority is an integral, ingrained, and necessary aspect of practicing law. Because persuasion is a key ingredient in successful representation, the corpus of texts to which legal practitioners make citation is understandably large. While citation to many of these texts are made to the page number on which the cited material appears, there are many instances when citation to non-page units of a text is required. 

The most notable of these is legislative texts, such as statutes and regulations, which are oftentimes broken down into a number of sections ("&sect;"). Courts in some jurisdictions number the paragraphs ("&para;") in their written decisions and cite to those instead of the page number. Transcripts in depositions usually number the lines on each page, so citation can be made thereto.

For example, the United States Code is initially divided among 54 Titles. And, per the Office of Law Revision Counsel of the U.S. House of Representatives, "\[t\]he basic unit of every Code title is the section" ("&sect;"). Additional units of citation include paragraph numbers ("&para;"). 

For example, an attorney in one recent case [argued](https://iowacapitaldispatch.com/2023/12/11/alleged-tree-thief-claims-protection-by-englands-charter-of-the-forest/) that England's 1217 Charter of the Forest 

The `pageStart` and `pageEnd` properties are useful for legal citations. However, in the large corpus of texts to which legal practitioners cite, the `pageStart` and `pageEnd` properties are insufficient.

### `pincite`, `citeUnit`, `pinciteRangeStart`, and `pinciteRangeEnd`

**Expected Type:** `Text`

**Description:** 

**Rationale:** The current properties `pageStart` and `pageEnd` are insufficient for two reasons. *First*, use of "page" in each property precludes reference to other document subdivisions, such as paragraphs, lines, sections, etc. *Second*, the descriptions of the `pageStart` and `pageEnd` properties explain that the relative reference is to the start or end of *the work*, as opposed to only a portion of the work.

## New Properties for `Message`

### `through`

**Expected Type:** `Audience` or `Organization` or `Person`

**Description:** An intermediary through which a message is sent. Commonly used in inter- and intra-office memoranda.

## New Properties for `Person`

### `generationalSuffix`

* Expected Type: `Text`
* Description: A suffix "used to distinguish persons who share the same name within a family" (_e.g._, "Jr.," "Sr.," "II," "III").  Distinct from `honorificSuffix`.
* Quoted source: Maryland Higher Education Commission Data Dictionary.

### `additionalNameInitial`

* Expected Type: `Text`
* Description: A single-letter initial used in place of, for example, a middle name.

### `familyNameInitial`

* Expected Type: `Text`
* Description: A single-letter initial used in place of a `familyName`.

### `givenNameInitial`

* Expected Type: `Text`
* Description: A single-letter initial used in place of a `givenName`.

### `neeName`

* Expected Type: `Text` or `Organization`
* Description: The word "née" is used to refer to the maiden `familyName` of a woman or the former name of something.
* Source: [Merriam-Webster.com](https://www.merriam-webster.com/dictionary/n%C3%A9e). Example sentences: "Mrs. Jane Doe, née Smith." "The Brewers née Pilots who are in their third year."


## New Properties for `Thing`

### `notarizedBy`

* Expected Type: `Person`
* Description: Indicates a notary has notarized the `Thing`.

## References

### _Ontologies and Document Models_

The Bibliographic Ontology ([link](https://dcmi.github.io/bibo/)). See the following Classes: [:Document](https://dcmi.github.io/bibo/#:Document); [:LegalDocument](https://dcmi.github.io/bibo/#:LegalDocument); [:LegalDecision](https://dcmi.github.io/bibo/#:LegalDecision); [:Legislation](https://dcmi.github.io/bibo/#:Legislation); [:PersonalCommunicationDocument](https://dcmi.github.io/bibo/#:PersonalCommunicationDocument).

Akoma Ntoso Version 1.0. Part 1: XML Vocabulary OASIS Standard (Aug. 28, 2018) ([link](http://docs.oasis-open.org/legaldocml/akn-core/v1.0/os/part1-vocabulary/akn-core-v1.0-os-part1-vocabulary.html#_Toc523925006)).

Akoma Ntoso Version 1.0. Part 1: XML Vocabulary Committee Specification 01 (Jun. 6, 2017) ([link](http://docs.oasis-open.org/legaldocml/akn-core/v1.0/cs01/part1-vocabulary/akn-core-v1.0-cs01-part1-vocabulary.html))

United States Legislative Markup: Review Guide for Version 2.0 of the USLM Schema (rev. ed. Apr. 11, 2023) ([link](https://github.com/usgpo/uslm/blob/main/USLM-2_0-Review-Guide-v2_0_12.pdf))

### _Issues and Threads Relating to Legislation_

[Issue 2698](https://github.com/schemaorg/schemaorg/issues/2698) - Extend the description of Legislation

[Issue 1743](https://github.com/schemaorg/schemaorg/issues/1743) - Refine/adjust the proposed "legal.schema.org" extension

[Issue 1736](https://github.com/schemaorg/schemaorg/issues/1736) - overly specific prop names/descriptions in Extensions

[Issue 1363](https://github.com/schemaorg/schemaorg/issues/1363) - Legislation: to harmonize proposed extension with AKN and LexML

[Issue 1156](https://github.com/schemaorg/schemaorg/issues/1156) - Legislation : Proposed extension

[Issue 1154](https://github.com/schemaorg/schemaorg/issues/1154) - Add "Legislation" as subclass of CreativeWork

### _Issues Relating to Legal Decisions_

[Issue 3404](https://github.com/schemaorg/schemaorg/issues/3404) - 'Decision' missing as Schema type?

[Issue 980](https://github.com/schemaorg/schemaorg/issues/980) - Vocabulary (or extension, community group etc.) for legal decisions and/or legislation

[Public w3 Mailing List](https://lists.w3.org/Archives/Public/public-schemaorg/2015May/0027.html) - vocabulary for legal decision (e.g., Supreme Court cases)

### _Issues Touching on the Legal Field_

[Issue 784](https://github.com/schemaorg/schemaorg/issues/784) - "Attorney" type is ambiguous, consider "Law Firm" or "Law Office" as another type of the business

[Issue 452](https://github.com/schemaorg/schemaorg/issues/452) - Legal Form (type of business) is missing for Organizations

[Issue 448](https://github.com/schemaorg/schemaorg/issues/448) - opengov.schema.org extension

### _Authorities on Citation, Etiquette, and Style_
The Bluebook: A Uniform System of Citation (21st ed. 2020)

The Supreme Court's Style Guide (Jack Metzler Ed. 2016) ([link](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2758862))

The Emily Post Institute, Guide to Writing Men's Names with Suffixes (n.d.) (accessed Mar. 17, 2024) ([link](https://emilypost.com/advice/mens-names-and-titles)).

### Other References

Maryland Higher Education Commission Data Dictionary (rev. ed. Oct. 10, 2013) ([link](https://data.mhec.state.md.us/MAC2Pilot/DDP/DD13.pdf))