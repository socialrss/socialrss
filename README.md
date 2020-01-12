# Social RSS Specification

Social RSS is an extension for RSS feeds that adds social network information.
For more information about this project, check the [about](https://github.com/socialrss/about) repository.

This repository holds the **Social RSS specification**, which is comprised of:
* A _XML Schema (XSD)_ defining the RSS XML extension - [`socialrss.xsd`](./socialrss.xsd)
* Extendend documentation in form of a Markdown file - [`DOCUMENTATION.md`](./DOCUMENTATION.md)
* Automated tests (which doubles as documentation) - See the section _Automated testing_ on this document

## Scope 

The current version of Social RSS includes:

* tags for the podcast and participants social networks and contacts
* tags for hashtags
* tags for for donation and crowdsourcing platforms (funding)
* tags for disqus threads

## Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"
	xmlns:atom="http://www.w3.org/2005/Atom"
	xmlns:social="http://socialrss.org/schemas/socialrss/1.0"
>
	<channel>
		<title>Your podcast title</title>
		<atom:link href="https://yourpodcast.com/feed" rel="self" type="application/rss+xml" />
		<link>https://yourpodcast.com</link>
		<description>Your podcast description.</description>
		<lastBuildDate>Wed, 10 Jan 2018 19:00:25 +0000</lastBuildDate>
		
		<!-- Contact and social network information-->
		<social:email>contact@yourpodcast.com</social:email>
		<social:handle type="twitter">yourpodcast</social:handle>
		<social:handle type="facebook.page">yourpodcast</social:handle>

		<!-- Crowdfunding -->
		<social:donation type="wallet.XBT">3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy</social:donation>
		<social:donation type="patreon">yourpodcast</social:donation>
		
		<!-- A PERMANENT participant, id is a unique identifier so that it can be used as a reference
		in the items -->
		<social:participant name="Participant 1" id="participant1" permanent="true">
			<social:email>participant1@yourpodcast.com</social:email>
			<social:handle type="twitter">paticipant1</social:handle>
			<social:handle type="facebook">paticipant1</social:handle>
		</social:participant>
		
		<!-- An EVENTUAL participant, id is a unique identifier so that it can be used as a reference
		in the items -->
		<social:participant name="Eventual Participant 2" id="participant2">
			<social:handle type="twitter">paticipant2</social:handle>
			<social:handle type="facebook">paticipant2</social:handle>
		</social:participant>

		<image>
			<url>http://yourpodcast.com/artwork.png</url>
		</image> 
		
		<item>
			<title>Episode 1</title>
			<link>http://yourpodcast.com/episode_post</link>
			<pubDate>Wed, 10 Jan 2018 16:58:41 +0000</pubDate>
			<guid isPermaLink="false">http://yourpodcast.com/episode_post</guid>
			<description>Episode description</description>
			<enclosure url="http://yourpodcast.com/episodes/episode1.mp3" length="72714941" type="audio/mpeg" />
			
			<!-- participants that are already defined in <channel> can be referred by id -->
			<social:participantReference id="participant1"/>
			<social:participantReference id="participant2"/>
			
			<!-- one time participants can be defined inside the item,
			if they become an eventual or permanent participant,
			they can be moved to <channel> and referred here -->
			<social:participant name="Guest">
				<social:email>guest@email.com</social:email>
				<social:handle type="twitter">guest</social:handle>
				<social:handle type="facebook">guest</social:handle>
			</social:participant>
			
			<!-- comment platforms integration seems too specific to have generic tags 
			so we have a specific disqus tag -->
			<social:disqus shortname="yourpodcast" page_url="http://yourpodcast.com/episode_post" page_identifier="episode1"/>
		</item>
	</channel>
</rss>
```

## Versioning

The versioning process for this specification is still not well defined.
This is a major task and it will be tracked with [issue #5](https://github.com/socialrss/socialrss/issues/5).

## Automated testing

This project containts a Python script (`test_schema.py`) to test the XML Schema agains sample XML Snippets.
For more information on automated testing roadmap and open issues for this project, check the issues with the label [`auto-test`](https://github.com/socialrss/socialrss/labels/auto-tests).

## Contributing to Social RSS

You will find general contribution guidelines [here](https://github.com/socialrss/.github/blob/master/CONTRIBUTING.md).

## Feature request, Support and Feedback

You will find information on general feature request, support and feedback processes [here](https://github.com/socialrss/.github/blob/master/SUPPORT.md).
