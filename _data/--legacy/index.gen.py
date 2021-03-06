## This script generates the file index.html


books=["Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy", "Joshua", "Judges", "1 Samuel", "2 Samuel", "1 Kings", "2 Kings", "Isaiah", "Jeremiah", "Ezekiel", "Hosea", "Joel", "Amos", "Obadiah", "Jonah", "Micah", "Nahum", "Habakkuk", "Zephaniah", "Haggai", "Zechariah", "Malachi", "Psalms", "Proverbs", "Job", "Song of Songs", "Ruth", "Lamentations", "Ecclesiastes", "Esther", "Daniel", "Ezra", "Nehemiah", "1 Chronicles", "2 Chronicles"]

with open("index.html","w+") as fout:
        fout.write(
"""<!DOCTYPE html>
<head>
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" type="image/png" href="/assets/img/favicon.png"/>

<title>Westminster Leningrad Codex for Linguists</title>
<meta name="description" content="Biblical Hebrew samples for linguists. Verses, phonetics, gloss translation, morphology codes, syntax trees.">

<!-- Google Fonts loaded here depending on setting in _data/options.yml true loads font, blank does not-->
<link href='//fonts.googleapis.com/css?family=Lato:400,400italic&amp;subset=cyrillic,latin-ext' rel='stylesheet' type='text/css'>
<link href='//fonts.googleapis.com/css?family=EB+Garamond:400,400italic&amp;subset=cyrillic,latin-ext' rel='stylesheet' type='text/css'>


<link rel="stylesheet" type="text/css" href="/css/tufte.css">
<link rel="stylesheet" type="text/css" href="/css/print.css" media="print">

<!---  <link rel="canonical" href="https://bh.seveleu.com/16"> ---->

  <link rel="alternate" type="application/rss+xml" title="Belarusian Arabic script" href="{{site.website}}/feed.xml" /><style>span#toc{padding: 9px;padding-left: 0px;display:inline-block;}</style>
</head>

<body>
<header>
<nav class="group"><a href="">
<h3>Biblical Hebrew for linguists</h3><h4>Strong's Lexicon</h4></a></nav>
</header>

<article class="group">
<p style="margin: 0px;background-color: #ffd42a;padding: 5px;width:33%;"></p>

<div style="display: flex;"><p style="margin-bottom:27px;"><span id="toc" style="font-family:sans-serif;">Law</span>""" + "".join(
["""<span id="toc"><a class="shadow" href="/v/"""+book.replace(" ","")+".1.1.html"+"""">""" +book+"</a></span>" for book in books[:5] ])+ """
</p></div>

<p style="margin: 0px;background-color: #ff7f2a;padding: 5px;width:38%;"></p>

<div style="display: flex;"><p style="margin-bottom:27px;"><span id="toc" style="font-family:sans-serif;">Prophets</span>""" + "".join(
["""<span id="toc"><a class="shadow" href="/v/"""+book.replace(" ","")+".1.1.html"+"""">""" +book+"</a></span>" for book in books[5:21] ])+ """
</p></div>

<p style="margin: 0px;background-color: #7296cc;padding: 5px;width:27%;"></p>


<div style="display: flex;"><p style="margin-bottom:27px;"><span id="toc" style="font-family:sans-serif;">Writings</span>""" + "".join(
["""<span id="toc"><a class="shadow" href="/v/"""+book.replace(" ","")+".1.1.html"+"""">""" +book+"</a></span>" for book in books[21:] ])+ """
</p></div>

<p style="margin: 0px;background-color: #ffd42a;padding: 5px;width:33%;"></p>

<div style="display: flex;"><p style="margin-bottom:27px;"><span id="toc" style="font-family:sans-serif;">Lexicon</span>
<span id="toc"><a class="shadow" href="https://strong.seveleu.com/lexicon.html">Lexicon</a></span>
</p></div>

<p style="margin: 0px;background-color: #ff7f2a;padding: 5px;width:25%;"></p>

<div style="display: flex;"><p style="margin-bottom:27px;"><span id="toc" style="font-family:sans-serif;">Preparatory materials for the Belarusian translation</span>
<span id="toc"><a class="shadow" href="/translatoraid/index.html">Gloss translations</a></span>
</p></div>
 
</article>

<span class="print-footer"> - Seveleu-Dubrovnik's copy of the BH sources. <a href="https://seveleu.com/pages/bh-resource">About</a> | <a href="https://www.mechon-mamre.org/p/pt/ptmp3prq.htm" target="_blank">Listen audio.</a></span>

<footer><hr class="slender"><div class="credits"><span><svg xmlns="https://www.w3.org/2000/svg"   width="15px" height="15px" viewBox="0 0 980 980"><circle cx="490" cy="490" r="440" fill="none" stroke="#000" stroke-width="100"/><path d="M219,428H350a150,150 0 1 1 0,125H219a275,275 0 1 0 0-125z"/></svg> 2020 Seveleu-Dubrovnik's copy of the BH sources. <a href="https://seveleu.com/pages/bh-resource" target="_blank">About</a> | <a href="https://www.mechon-mamre.org/p/pt/ptmp3prq.htm" target="_blank">Listen audio</a>  | <a title="GitHub" href="https://github.com/wlcling/wlcling.github.io" target="_blank"><svg height="17" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="24" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path></svg></a></div></footer>

</body></html>""" )


