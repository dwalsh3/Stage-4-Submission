# Dan's light adaptation of Andy's Code Generator
# Submitted via github 8/12/2015

def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)


title1       =   "<h2>1. Web Basics</h2>"
description1 = '''<h3>How the Web Works</h3>
    <p>The web is a set of computers that communicate with each other. To visit page, a computer sends an <em>HTTP Request</em> to a <em>server</em>. The server finds the appropriate HTML document and sends it back to the computer where a <em>web browser</em>      interprets the page and displays it on the screen.
      <a href="https://www.udacity.com/course/viewer#!/c-ud721/l-3508959201/e-48329854/m-48480496">This video</a> explains it.
    </p>
    <h3>HTML</h3>
    <p>HTML stands for <em>Hypertext Markup Language.</em> HTML documents form the majority of the content on the web. HTML documents contain <em>text content</em> which describes "what you see" and <em>markup</em> which describes "how it looks".
      <a href="https://www.udacity.com/course/viewer#!/c-ud721/l-3508959201/m-48724340"> Overview </a>
    </p>
    <h3>Tags and Elements</h3>
    <p>HTML documents are made of HTML <b>elements</b>. When writing HTML, we tell browsers the type of each element by using HTML <b>tags</b>.
      <a href="https://www.udacity.com/course/viewer#!/c-ud721/l-3508959201/m-48723444">This video</a> explains.
    </p>
    <h3>Why Computers are Literal</h3>
    <p>Some people call computers stupid because they interpret instructions literally. I don't mind.
    </p>
    <h3>Inline vs Block Elements</h3>
    <p>HTML elements are either <b>inline</b> or <b>block</b>. Block elements form an "invisible box" around the content inside of them.
    </p>.'''

title2       =   "<h2>2. Structure - HTML</h2>"
description2 = '''<h3>Document Structure and the House Analogy</h3>
    <p>The following describes the relationship bewteen HTML and the visual structure of a page. HTML is the walls, CSS is the color of the paint, and JavaScript is the electrical system.</p>
    <ul>
      <li>Not all elements are visible.</li>
      <li>All visible elements are rectangular</li>
      <li>HTML uses a tree structure.</li>
      <li>DOM: Document Object Model</li>
    </ul>
    <h3>HTML Code style</h3>
    <p><b>Lower Case Names:</b> It's more efficient to code all classes, attributes, and tags with lower case letters because it's faster to read and faster to code:
    </p>
    <div class=block-quote>
      div id="num-1" class="article" tabindex=4
      <br> vs
      <br> div iD="NUM-1" Class="Article" TABINDEX=4>'''

title3       =   "<h2> 3. Style - CSS </h2>"
description3 = '''<h3>Linking Style to Content</h3>
    <script src="https://gist.github.com/dwalsh3/3a4ed6ef6a44a59bb8c5.js"></script>
    <h3>How to Display Code ^</h3>
    <p>Showing code in a webpage takes some thought -- the browser will execute it unless it's wrapped in something, or, in this case, embeded from an external site. Github works <a href="https://gist.github.com/dwalsh3/3a4ed6ef6a44a59bb8c5#file-gistfile1-txt"> alright</a>,
      but I'm looking forward to something with <b>syntax highlighting</b>. Also, I don't know javascript yet, so script above is a bit of a black box at this point.</p>


    <p>If you want to do it the old fashioned way, The less than (&lt;) and greater than (&gt;) signs are special characters in HTML, denoting tags. How do we insert them as readable text? We have to use a special sequence of characters.</p>
    <div class=block-quote>
      <p>"& l t ;" (without spaces) will show up as &lt; </p>
      <p>"& g t ;"(without spaces) will show up as &gt;.</p>
    </div>
    <h3><span class=rainbow>Gay Marriage is Now Legal in the Entire United States!</span></h3>
    <p>It may have nothing to do with the course, but it's going in anyway. At 10am today, June 26, 2015, the Supreme Court overturned all remaining state bans on gay marriage.</p>
    <p>Github and Stack Overflow are getting in on the exitement, so why not me?</p>
    <img class=gay-img src="http://i.imgur.com/HDzQxZL.png" alt="gay stack overflow">
    <img class=gay-img src="http://imgur.com/E9oe7sW.png" alt="gay github">
    <h3>CSS Code Style</h3>
    <p><b>One Attribute per Line:</b> For development code, it's good to have one attribute per line. We should never put more than one attribute per line to make things easier to read.</p>
    <h3>Color Pickin'</h3>
    <p>Here's a useful color picker I found: <a href="http://www.w3schools.com/tags/ref_colorpicker.asp">w3schools color picker </a></p>
    <p>Another interesting tidbit I picked up while creating this page is that hex color codes can be written shorthand when they're made of three repeating pairs. #ABC is interpreted as #AABBCC.</p>
    <h3>Don't Repeat Yourself</h3> Repeating oneself in CSS is worse than a waste of time--it's dangerous. Changing something like the body's margins should be a simple process, but if a site is designed with multiple, repetative divs, that simple task could become long and fraught.
    That's why I was surprised to be unable to find a parsimonious method of obtaining this page's alternating grey and white background colors. Even though the text margins stay the same throughout, each div must be full-width to allow the background
    color extend to the screen's edge. Hmm. Now that I think about it, maybe it's possible for background color to extend past the padded box by applying negative values to the relevant parameter. Will try that next submission. For now, I'm using multiple
    classes, one of which adds grey, for each lesson div. But even the grey seems to need the same margin parameters.*
    <p>*And fixed. Of course it didn't need the inherited parameters.</p>'''



EXAMPLE_LIST_OF_CONCEPTS = [ [title1, description1],
                             [title2, description2],
                             [title3, description3]] 


def make_HTML_for_many_concepts(list_of_concepts):
    HTML = ""
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML

print make_HTML_for_many_concepts(EXAMPLE_LIST_OF_CONCEPTS)
