# Documentation

## `<email>`

The `<email>` tag can be specified in the `<channel>` or `<participant>` tags.  
It can only be specificed once under these tags.

## `<handle>` tag

The `<handle>` tag is a generic tag for social network handles.  
Multiple `<handle>` tags can be specified in the `<channel>`, `<item>` 
or `<participant>` tags.

### Example

```xml
<handle type="twitter" url="https://twitter.com/podcast" text="Twitter">podcast</handle>
```

### Attributes

| Attribute | Description                                                    |
|-----------|----------------------------------------------------------------|
| type      | (required) type of the handle                                  |
| url       | Url corresponding to the handle, i.e.: the twitter account url |
| text      | Text that defines the handle type                              |

Url and text are not required but recommended.  
If the aggregtor is not designed to support the specified type, it can use url and text
in a generic manner to still provide some usability.

#### Reserved types

| Type               | Description          | Additional information                                  |
|--------------------|----------------------|---------------------------------------------------------|
| twitter            | Twitter account      | Intended for use under `<channel>` and `<participant>`  |
| twitter.tweet      | Tweet                | Intended for use under `<item>`                         |
| facebook           | Facebook profile     | Intended for use under `<participant>`                  |
| facebook.page      | Facebook page        | Intended for use under `<channel>`                      |
| facebook.group     | Facebook group       | Intended for use under `<channel>`                      |
| instagram          | Instagram            | Intended for use under `<channel>` and `<participant>`  |
| telegram           | Telegram user        | Intended for use under `<participant>`                  |
| telegram.group     | Telegram group       | Intended for use under `<channel>`                      |
| youtube.channel    | Youtube channel      | Intended for use under `<channel>` and `<participant>`  |

## `<hashtag>` tag

The `<hashtag>` tag is used to add hashtags to the podcast or episodes.  
It can be specified in the `<channel>` or `<item>` tags.

## `<donation>` tag

The `<crowdfunding>` tag is used for handles of donation or crowdfunding platforms, including
cryptocurrency wallet addresses.  
The `<crowdfunding>`tag can be specified in the `<channel>` tag.

### Examples

#### Patreon

```xml
<donation type="patreon" url="https://www.patreon.com/podcast" text="Patreon">podcast</donation>
```

#### Bitcoin Wallet

```xml
<donation type="wallet.XBT" text="Bitcoin">1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2</donation>
```

### Attributes

| Attribute | Description                                                      |
|-----------|------------------------------------------------------------------|
| type      | (required) type of the donation                                  |
| url       | Url corresponding to the donation, i.e.: the twitter account url |
| text      | Text that defines the donation type                              |

Url and text are not required but recommended.  
If the aggregtor is not designed to support the specified type, it can use url and text
in a generic manner to still provide some usability.

#### Reserved types

| Type               | Description                                             |
|--------------------|---------------------------------------------------------|
| wallet.`<currency>`| Cryptocurrency wallet                                   |
| paypal             | [Paypal](https://paypal.com)                            |
| patreon            | [Patreon](https://patreon.com)                          |
| apoiase            | [Apoia.se](https://apoia.se)                            |
| padrim             | [Padrim](https://www.padrim.com.br)                     |
| pagseguro          | [PagSeguro](https://pagseguro.com.br)                   |
| picpay             | [PicPay](https://www.picpay.com)                        |

## `<participant>` tag

The `<participant>` tag can be specified multiple times in 
the `<channel>` or `<item>` tag.

The participant tag `<participant>` can contain one `<email>` and multiple `<handle>` tags.

### Example

```xml
<participant name="Participant Name" id="participant1" permanent="true">
	<email>participant1@podcast.com</email>
	<handle type="twitter" url="https://twitter.com/participant1" text="Twitter">participant1</handle>
</participant>
```

### Attributes

| Attribute | Description                                                      |
|-----------|------------------------------------------------------------------|
| name      | _(required)_ Participant name type of the donation               |
| id        | Participant id, to be referred by `<participantReference>` tags  |
| permanent | _(boolean)_ To be used only under `<channel>`, to indicate it is a fixed participant |

Url and text are not required but recommended.  
If the aggregtor is not designed to support the specified type, it can use url and text
in a generic manner to still provide some usability.

## `<participantReference>` tag

The `<participant>` tag can be specified multiple times in the `<item>` tag.
It refers to an already declared participant under the `<channel>` tag.

### Example

```xml
<channel>
	...
	<participant name="Participant Name" id="participant1" permanent="true">
		<email>participant1@podcast.com</email>
		<handle type="twitter" url="https://twitter.com/participant1" text="Twitter">participant1</handle>
	</participant>
	...
	<item>
		...
		<participantReference id="participant1"/>
		...
	</item>
	<item>
		...
		<participantReference id="participant1"/>
		...
	</item>
</channel>
```

## `<disqus>` tag

The `<disqus>` tag can be specified once in `<item>` tags.

### Example

```xml
<disqus shortname="podcast" page_url="https://podcast.com/post1" page_identifier="post1id"/>
```

### Attributes

The attributes shortname, page_url and page_identifier correspond to the attributes as shown below in the
disqus [Universal Embed Code](https://help.disqus.com/customer/portal/articles/472097-universal-embed-code).

```javascript
var disqus_config = function () {
        // Replace PAGE_URL with your page's canonical URL variable
        this.page.url = PAGE_URL;  
        
        // Replace PAGE_IDENTIFIER with your page's unique identifier variable
        this.page.identifier = PAGE_IDENTIFIER; 
    };
    
    (function() {  // REQUIRED CONFIGURATION VARIABLE: EDIT THE SHORTNAME BELOW
        var d = document, s = d.createElement('script');
        
        // IMPORTANT: Replace EXAMPLE with your forum shortname!
        s.src = 'https://SHORT_NAME.disqus.com/embed.js';
        
        s.setAttribute('data-timestamp', +new Date());
        (d.head || d.body).appendChild(s);
    })();
```