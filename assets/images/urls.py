<!DOCTYPE html>
<html class=" mdzr-js mdzr-borderradius mdzr-boxshadow mdzr-cssanimations mdzr-svg" lang="en"><head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="ROBOTS" content="ALL">
    <meta name="MSSmartTagsPreventParsing" content="true">
    <meta name="Copyright" content="Django Software Foundation">
    <meta name="keywords" content="Python, Django, framework, open-source">
    <meta name="description" content="">

    
  
    
      
    
  
  <link rel="canonical" href="https://docs.djangoproject.com/en/2.2/intro/tutorial01/">
  
    
      
    
    <link rel="alternate" hreflang="el" href="https://docs.djangoproject.com/el/2.2/intro/tutorial01/">
  
    
      
    
    <link rel="alternate" hreflang="en" href="https://docs.djangoproject.com/en/2.2/intro/tutorial01/">
  
    
      
    
    <link rel="alternate" hreflang="es" href="https://docs.djangoproject.com/es/2.2/intro/tutorial01/">
  
    
      
    
    <link rel="alternate" hreflang="fr" href="https://docs.djangoproject.com/fr/2.2/intro/tutorial01/">
  
    
      
    
    <link rel="alternate" hreflang="id" href="https://docs.djangoproject.com/id/2.2/intro/tutorial01/">
  
    
      
    
    <link rel="alternate" hreflang="ja" href="https://docs.djangoproject.com/ja/2.2/intro/tutorial01/">
  
    
      
    
    <link rel="alternate" hreflang="ko" href="https://docs.djangoproject.com/ko/2.2/intro/tutorial01/">
  
    
      
    
    <link rel="alternate" hreflang="pl" href="https://docs.djangoproject.com/pl/2.2/intro/tutorial01/">
  
    
      
    
    <link rel="alternate" hreflang="pt-br" href="https://docs.djangoproject.com/pt-br/2.2/intro/tutorial01/">
  
    
      
    
    <link rel="alternate" hreflang="zh-hans" href="https://docs.djangoproject.com/zh-hans/2.2/intro/tutorial01/">
  

  <link rel="search" type="application/opensearchdescription+xml" href="https://docs.djangoproject.com/en/2.2/search/description/" title="Django documentation">

    <!-- Favicons -->
    <link rel="apple-touch-icon" href="https://static.djangoproject.com/img/icon-touch.e4872c4da341.png">
    <link rel="icon" sizes="192x192" href="https://static.djangoproject.com/img/icon-touch.e4872c4da341.png">
    <link rel="shortcut icon" href="https://static.djangoproject.com/img/favicon.6dbf28c0650e.ico">
    <meta name="msapplication-TileColor" content="#113228">
    <meta name="msapplication-TileImage" content="https://static.djangoproject.com/img/icon-tile.b01ac0ef9f67.png">

    <title>Writing your first Django app, part 1 | Django documentation | Django</title>

    <link rel="stylesheet" href="urls_files/output.css">
    <script src="urls_files/webfontloader.js"></script>
    <link rel="stylesheet" href="urls_files/css.css"><script>
    WebFont.load({
      custom: {
        families: ['FontAwesome', 'Fira+Mono'],
      },
      google: {
        families: ['Roboto:400italic,700italic,300,700,400:latin'
        ]
      },
      classes: false,
      events: false,
      timeout: 1000
    });
    </script>
    <script src="urls_files/modernizr.js"></script>
    
  <script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="main.07884ebc4865" src="urls_files/main.js"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="mod/mobile-menu" src="urls_files/mobile-menu.js"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="mod/version-switcher" src="urls_files/version-switcher.js"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="mod/search-key" src="urls_files/search-key.js"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="mod/clippify" src="urls_files/clippify.js"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="mod/console-tabs" src="urls_files/console-tabs.js"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="jquery" src="urls_files/jquery.js"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="clipboard" src="urls_files/clipboard.js"></script></head>

  <body id="generic" class="">

    <div role="banner" id="top">
  <div class="container">
    <a class="logo" href="https://www.djangoproject.com/">Django</a>
    <p class="meta">The web framework for perfectionists with deadlines.</p>
    <div class="menu-button"><i class="icon icon-reorder"></i><span>Menu</span></div><div role="navigation" class="nav-menu-on">
      <ul>
        <li>
          <a href="https://www.djangoproject.com/start/overview/">Overview</a>
        </li>
        <li>
          <a href="https://www.djangoproject.com/download/">Download</a>
        </li>
        <li class="active">
          <a href="https://docs.djangoproject.com/">Documentation</a>
        </li>
        <li>
          <a href="https://www.djangoproject.com/weblog/">News</a>
        </li>
        <li>
          <a href="https://www.djangoproject.com/community/">Community</a>
        </li>
        <li>
          <a href="https://code.djangoproject.com/">Code</a>
        </li>
        <li>
          <a href="https://www.djangoproject.com/foundation/">About</a>
        </li>
        <li>
          <a href="https://www.djangoproject.com/fundraising/">♥ Donate</a>
        </li>
      </ul>
    </div>
  </div>
</div>


    <div class="copy-banner">
      <div class="container">
        
  <h1><a href="https://docs.djangoproject.com/en/2.2/">Documentation</a></h1>

      </div>
    </div>
    <div id="billboard"></div>

    <div class="container sidebar-right">
      <div role="main">

        
          
        

        
<div id="version-switcher">
  <ul id="doc-languages" class="language-switcher">
  
  
  <li class="other">
    
      
    
    <a href="https://docs.djangoproject.com/el/2.2/intro/tutorial01/">el</a>
  </li>
  
  
  
  
  
  <li class="other">
    
      
    
    <a href="https://docs.djangoproject.com/es/2.2/intro/tutorial01/">es</a>
  </li>
  
  
  
  <li class="other">
    
      
    
    <a href="https://docs.djangoproject.com/fr/2.2/intro/tutorial01/">fr</a>
  </li>
  
  
  
  <li class="other">
    
      
    
    <a href="https://docs.djangoproject.com/id/2.2/intro/tutorial01/">id</a>
  </li>
  
  
  
  <li class="other">
    
      
    
    <a href="https://docs.djangoproject.com/ja/2.2/intro/tutorial01/">ja</a>
  </li>
  
  
  
  <li class="other">
    
      
    
    <a href="https://docs.djangoproject.com/ko/2.2/intro/tutorial01/">ko</a>
  </li>
  
  
  
  <li class="other">
    
      
    
    <a href="https://docs.djangoproject.com/pl/2.2/intro/tutorial01/">pl</a>
  </li>
  
  
  
  <li class="other">
    
      
    
    <a href="https://docs.djangoproject.com/pt-br/2.2/intro/tutorial01/">pt-br</a>
  </li>
  
  
  
  <li class="other">
    
      
    
    <a href="https://docs.djangoproject.com/zh-hans/2.2/intro/tutorial01/">zh-hans</a>
  </li>
  
  
    <li class="current" title="Click on the links on the left to switch to another language.">
      <span>Language: <strong>en</strong></span>
    </li>
  </ul>

  
  <ul id="doc-versions" class="version-switcher">
    
    
    <li class="other">
      
        
      
      <a href="https://docs.djangoproject.com/en/1.7/intro/tutorial01/">1.7</a>
    </li>
    
    
    
    <li class="other">
      
        
      
      <a href="https://docs.djangoproject.com/en/1.8/intro/tutorial01/">1.8</a>
    </li>
    
    
    
    <li class="other">
      
        
      
      <a href="https://docs.djangoproject.com/en/1.9/intro/tutorial01/">1.9</a>
    </li>
    
    
    
    <li class="other">
      
        
      
      <a href="https://docs.djangoproject.com/en/1.10/intro/tutorial01/">1.10</a>
    </li>
    
    
    
    <li class="other">
      
        
      
      <a href="https://docs.djangoproject.com/en/1.11/intro/tutorial01/">1.11</a>
    </li>
    
    
    
    <li class="other">
      
        
      
      <a href="https://docs.djangoproject.com/en/2.0/intro/tutorial01/">2.0</a>
    </li>
    
    
    
    <li class="other">
      
        
      
      <a href="https://docs.djangoproject.com/en/2.1/intro/tutorial01/">2.1</a>
    </li>
    
    
    
    
    
    <li class="other">
      
        
      
      <a href="https://docs.djangoproject.com/en/dev/intro/tutorial01/">dev</a>
    </li>
    
    
    <li class="current" title="This document describes Django 2.2. Click on the links on the left to see other versions.">
       <span>Documentation version:
         <strong>2.2</strong>
       </span>
    </li>
  </ul>
</div>


<div id="docs-content">
<div class="section" id="s-writing-your-first-django-app-part-1">
<span id="writing-your-first-django-app-part-1"></span><h1>Writing your first Django app, part 1<a class="headerlink" href="#writing-your-first-django-app-part-1" title="Permalink to this headline">¶</a></h1>
<p>Let’s learn by example.</p>
<p>Throughout this tutorial, we’ll walk you through the creation of a basic
poll application.</p>
<p>It’ll consist of two parts:</p>
<ul class="simple">
<li>A public site that lets people view polls and vote in them.</li>
<li>An admin site that lets you add, change, and delete polls.</li>
</ul>
<p>We’ll assume you have <a class="reference internal" href="https://docs.djangoproject.com/en/2.2/intro/install/"><span class="doc">Django installed</span></a> already. You can
tell Django is installed and which version by running the following command
in a shell prompt (indicated by the $ prefix):</p>
<div class="console-block" id="console-block-0">
<input class="c-tab-unix" id="c-tab-0-unix" type="radio" name="console-0" checked="checked">
<label for="c-tab-0-unix" title="Linux/macOS">/</label>
<input class="c-tab-win" id="c-tab-0-win" type="radio" name="console-0">
<label for="c-tab-0-win" title="Windows"></label>
<section class="c-content-unix" id="c-content-0-unix">
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$</span> python -m django --version
</pre></div>
</div>
</section>
<section class="c-content-win" id="c-content-0-win">
<div class="highlight"><pre><span></span><span class="gp">...\&gt;</span> py -m django --version
</pre></div>
</section>
</div>
<p>If Django is installed, you should see the version of your installation. If it
isn’t, you’ll get an error telling “No module named django”.</p>
<p>This tutorial is written for Django 2.2, which supports Python 3.5 and
later. If the Django version doesn’t match, you can refer to the tutorial for
your version of Django by using the version switcher at the bottom right corner
of this page, or update Django to the newest version. If you’re using an older
version of Python, check <a class="reference internal" href="https://docs.djangoproject.com/en/2.2/faq/install/#faq-python-version-support"><span class="std std-ref">What Python version can I use with Django?</span></a> to find a compatible
version of Django.</p>
<p>See <a class="reference internal" href="https://docs.djangoproject.com/en/2.2/topics/install/"><span class="doc">How to install Django</span></a> for advice on how to remove
older versions of Django and install a newer one.</p>
<div class="admonition-where-to-get-help admonition">
<p class="first admonition-title">Where to get help:</p>
<p class="last">If you’re having trouble going through this tutorial, please post a message
to <a class="reference internal" href="https://docs.djangoproject.com/en/2.2/internals/mailing-lists/#django-users-mailing-list"><span class="std std-ref">django-users</span></a> or drop by <a class="reference external" href="irc://irc.freenode.net/django">#django on irc.freenode.net</a> to chat with other Django users who might
be able to help.</p>
</div>
<div class="section" id="s-creating-a-project">
<span id="creating-a-project"></span><h2>Creating a project<a class="headerlink" href="#creating-a-project" title="Permalink to this headline">¶</a></h2>
<p>If this is your first time using Django, you’ll have to take care of some
initial setup. Namely, you’ll need to auto-generate some code that establishes a
Django <a class="reference internal" href="https://docs.djangoproject.com/en/2.2/glossary/#term-project"><span class="xref std std-term">project</span></a> – a collection of settings for an instance of Django,
including database configuration, Django-specific options and
application-specific settings.</p>
<p>From the command line, <code class="docutils literal notranslate"><span class="pre">cd</span></code> into a directory where you’d like to store your
code, then run the following command:</p>
<div class="console-block" id="console-block-1">
<input class="c-tab-unix" id="c-tab-1-unix" type="radio" name="console-1" checked="checked">
<label for="c-tab-1-unix" title="Linux/macOS">/</label>
<input class="c-tab-win" id="c-tab-1-win" type="radio" name="console-1">
<label for="c-tab-1-win" title="Windows"></label>
<section class="c-content-unix" id="c-content-1-unix">
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$</span> django-admin startproject mysite
</pre></div>
</div>
</section>
<section class="c-content-win" id="c-content-1-win">
<div class="highlight"><pre><span></span><span class="gp">...\&gt;</span> django-admin startproject mysite
</pre></div>
</section>
</div>
<p>This will create a <code class="docutils literal notranslate"><span class="pre">mysite</span></code> directory in your current directory. If it didn’t
work, see <a class="reference internal" href="https://docs.djangoproject.com/en/2.2/faq/troubleshooting/#troubleshooting-django-admin"><span class="std std-ref">Problems running django-admin</span></a>.</p>
<div class="admonition note">
<p class="first admonition-title">Note</p>
<p class="last">You’ll need to avoid naming projects after built-in Python or Django
components. In particular, this means you should avoid using names like
<code class="docutils literal notranslate"><span class="pre">django</span></code> (which will conflict with Django itself) or <code class="docutils literal notranslate"><span class="pre">test</span></code> (which
conflicts with a built-in Python package).</p>
</div>
<div class="admonition-where-should-this-code-live admonition">
<p class="first admonition-title">Where should this code live?</p>
<p>If your background is in plain old PHP (with no use of modern frameworks),
you’re probably used to putting code under the Web server’s document root
(in a place such as <code class="docutils literal notranslate"><span class="pre">/var/www</span></code>). With Django, you don’t do that. It’s
not a good idea to put any of this Python code within your Web server’s
document root, because it risks the possibility that people may be able
to view your code over the Web. That’s not good for security.</p>
<p class="last">Put your code in some directory <strong>outside</strong> of the document root, such as
<code class="file docutils literal notranslate"><span class="pre">/home/mycode</span></code>.</p>
</div>
<p>Let’s look at what <a class="reference internal" href="https://docs.djangoproject.com/en/2.2/ref/django-admin/#django-admin-startproject"><code class="xref std std-djadmin docutils literal notranslate"><span class="pre">startproject</span></code></a> created:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">mysite</span><span class="o">/</span>
    <span class="n">manage</span><span class="o">.</span><span class="n">py</span>
    <span class="n">mysite</span><span class="o">/</span>
        <span class="fm">__init__</span><span class="o">.</span><span class="n">py</span>
        <span class="n">settings</span><span class="o">.</span><span class="n">py</span>
        <span class="n">urls</span><span class="o">.</span><span class="n">py</span>
        <span class="n">wsgi</span><span class="o">.</span><span class="n">py</span>
</pre></div>
</div>
<p>These files are:</p>
<ul class="simple">
<li>The outer <code class="file docutils literal notranslate"><span class="pre">mysite/</span></code> root directory is just a container for your
project. Its name doesn’t matter to Django; you can rename it to anything
you like.</li>
<li><code class="file docutils literal notranslate"><span class="pre">manage.py</span></code>: A command-line utility that lets you interact with this
Django project in various ways. You can read all the details about
<code class="file docutils literal notranslate"><span class="pre">manage.py</span></code> in <a class="reference internal" href="https://docs.djangoproject.com/en/2.2/ref/django-admin/"><span class="doc">django-admin and manage.py</span></a>.</li>
<li>The inner <code class="file docutils literal notranslate"><span class="pre">mysite/</span></code> directory is the actual Python package for your
project. Its name is the Python package name you’ll need to use to import
anything inside it (e.g. <code class="docutils literal notranslate"><span class="pre">mysite.urls</span></code>).</li>
<li><code class="file docutils literal notranslate"><span class="pre">mysite/__init__.py</span></code>: An empty file that tells Python that this
directory should be considered a Python package. If you’re a Python beginner,
read <a class="reference external" href="https://docs.python.org/3/tutorial/modules.html#tut-packages" title="(in Python v3.7)"><span class="xref std std-ref">more about packages</span></a> in the official Python docs.</li>
<li><code class="file docutils literal notranslate"><span class="pre">mysite/settings.py</span></code>: Settings/configuration for this Django
project.  <a class="reference internal" href="https://docs.djangoproject.com/en/2.2/topics/settings/"><span class="doc">Django settings</span></a> will tell you all about how settings
work.</li>
<li><code class="file docutils literal notranslate"><span class="pre">mysite/urls.py</span></code>: The URL declarations for this Django project; a
“table of contents” of your Django-powered site. You can read more about
URLs in <a class="reference internal" href="https://docs.djangoproject.com/en/2.2/topics/http/urls/"><span class="doc">URL dispatcher</span></a>.</li>
<li><code class="file docutils literal notranslate"><span class="pre">mysite/wsgi.py</span></code>: An entry-point for WSGI-compatible web servers to
serve your project. See <a class="reference internal" href="https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/"><span class="doc">How to deploy with WSGI</span></a> for more details.</li>
</ul>
</div>
<div class="section" id="s-the-development-server">
<span id="the-development-server"></span><h2>The development server<a class="headerlink" href="#the-development-server" title="Permalink to this headline">¶</a></h2>
<p>Let’s verify your Django project works. Change into the outer <code class="file docutils literal notranslate"><span class="pre">mysite</span></code> directory, if
you haven’t already, and run the following commands:</p>
<div class="console-block" id="console-block-2">
<input class="c-tab-unix" id="c-tab-2-unix" type="radio" name="console-2" checked="checked">
<label for="c-tab-2-unix" title="Linux/macOS">/</label>
<input class="c-tab-win" id="c-tab-2-win" type="radio" name="console-2">
<label for="c-tab-2-win" title="Windows"></label>
<section class="c-content-unix" id="c-content-2-unix">
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$</span> python manage.py runserver
</pre></div>
</div>
</section>
<section class="c-content-win" id="c-content-2-win">
<div class="highlight"><pre><span></span><span class="gp">...\&gt;</span> py manage.py runserver
</pre></div>
</section>
</div>
<p>You’ll see the following output on the command line:</p>
<pre class="literal-block">Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.

July 02, 2019 - 15:50:53
Django version 2.2, using settings 'mysite.settings'
Starting development server at <a class="reference external" href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a>
Quit the server with CONTROL-C.
</pre>
<div class="admonition note">
<p class="first admonition-title">Note</p>
<p class="last">Ignore the warning about unapplied database migrations for now; we’ll deal
with the database shortly.</p>
</div>
<p>You’ve started the Django development server, a lightweight Web server written
purely in Python. We’ve included this with Django so you can develop things
rapidly, without having to deal with configuring a production server – such as
Apache – until you’re ready for production.</p>
<p>Now’s a good time to note: <strong>don’t</strong> use this server in anything resembling a
production environment. It’s intended only for use while developing. (We’re in
the business of making Web frameworks, not Web servers.)</p>
<p>Now that the server’s running, visit <a class="reference external" href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a> with your Web
browser. You’ll see a “Congratulations!” page, with a rocket taking off.
It worked!</p>
<div class="admonition-changing-the-port admonition">
<p class="first admonition-title">Changing the port</p>
<p>By default, the <a class="reference internal" href="https://docs.djangoproject.com/en/2.2/ref/django-admin/#django-admin-runserver"><code class="xref std std-djadmin docutils literal notranslate"><span class="pre">runserver</span></code></a> command starts the development server
on the internal IP at port 8000.</p>
<p>If you want to change the server’s port, pass
it as a command-line argument. For instance, this command starts the server
on port 8080:</p>
<div class="console-block" id="console-block-3">
<input class="c-tab-unix" id="c-tab-3-unix" type="radio" name="console-3" checked="checked">
<label for="c-tab-3-unix" title="Linux/macOS">/</label>
<input class="c-tab-win" id="c-tab-3-win" type="radio" name="console-3">
<label for="c-tab-3-win" title="Windows"></label>
<section class="c-content-unix" id="c-content-3-unix">
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$</span> python manage.py runserver <span class="m">8080</span>
</pre></div>
</div>
</section>
<section class="c-content-win" id="c-content-3-win">
<div class="highlight"><pre><span></span><span class="gp">...\&gt;</span> py manage.py runserver 8080
</pre></div>
</section>
</div>
<p>If you want to change the server’s IP, pass it along with the port. For
example, to listen on all available public IPs (which is useful if you are
running Vagrant or want to show off your work on other computers on the
network), use:</p>
<div class="console-block" id="console-block-4">
<input class="c-tab-unix" id="c-tab-4-unix" type="radio" name="console-4" checked="checked">
<label for="c-tab-4-unix" title="Linux/macOS">/</label>
<input class="c-tab-win" id="c-tab-4-win" type="radio" name="console-4">
<label for="c-tab-4-win" title="Windows"></label>
<section class="c-content-unix" id="c-content-4-unix">
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$</span> python manage.py runserver <span class="m">0</span>:8000
</pre></div>
</div>
</section>
<section class="c-content-win" id="c-content-4-win">
<div class="highlight"><pre><span></span><span class="gp">...\&gt;</span> py manage.py runserver 0:8000
</pre></div>
</section>
</div>
<p class="last"><strong>0</strong> is a shortcut for <strong>0.0.0.0</strong>. Full docs for the development server
can be found in the <a class="reference internal" href="https://docs.djangoproject.com/en/2.2/ref/django-admin/#django-admin-runserver"><code class="xref std std-djadmin docutils literal notranslate"><span class="pre">runserver</span></code></a> reference.</p>
</div>
<div class="admonition-automatic-reloading-of-djadmin-runserver admonition">
<p class="first admonition-title">Automatic reloading of <a class="reference internal" href="https://docs.djangoproject.com/en/2.2/ref/django-admin/#django-admin-runserver"><code class="xref std std-djadmin docutils literal notranslate"><span class="pre">runserver</span></code></a></p>
<p class="last">The development server automatically reloads Python code for each request
as needed. You don’t need to restart the server for code changes to take
effect. However, some actions like adding files don’t trigger a restart,
so you’ll have to restart the server in these cases.</p>
</div>
</div>
<div class="section" id="s-creating-the-polls-app">
<span id="creating-the-polls-app"></span><h2>Creating the Polls app<a class="headerlink" href="#creating-the-polls-app" title="Permalink to this headline">¶</a></h2>
<p>Now that your environment – a “project” – is set up, you’re set to start
doing work.</p>
<p>Each application you write in Django consists of a Python package that follows
a certain convention. Django comes with a utility that automatically generates
the basic directory structure of an app, so you can focus on writing code
rather than creating directories.</p>
<div class="admonition-projects-vs-apps admonition">
<p class="first admonition-title">Projects vs. apps</p>
<p class="last">What’s the difference between a project and an app? An app is a Web
application that does something – e.g., a Weblog system, a database of
public records or a simple poll app. A project is a collection of
configuration and apps for a particular website. A project can contain
multiple apps. An app can be in multiple projects.</p>
</div>
<p>Your apps can live anywhere on your <a class="reference external" href="https://docs.python.org/3/tutorial/modules.html#tut-searchpath" title="(in Python v3.7)"><span class="xref std std-ref">Python path</span></a>. In
this tutorial, we’ll create our poll app right next to your <code class="file docutils literal notranslate"><span class="pre">manage.py</span></code>
file so that it can be imported as its own top-level module, rather than a
submodule of <code class="docutils literal notranslate"><span class="pre">mysite</span></code>.</p>
<p>To create your app, make sure you’re in the same directory as <code class="file docutils literal notranslate"><span class="pre">manage.py</span></code>
and type this command:</p>
<div class="console-block" id="console-block-5">
<input class="c-tab-unix" id="c-tab-5-unix" type="radio" name="console-5" checked="checked">
<label for="c-tab-5-unix" title="Linux/macOS">/</label>
<input class="c-tab-win" id="c-tab-5-win" type="radio" name="console-5">
<label for="c-tab-5-win" title="Windows"></label>
<section class="c-content-unix" id="c-content-5-unix">
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$</span> python manage.py startapp polls
</pre></div>
</div>
</section>
<section class="c-content-win" id="c-content-5-win">
<div class="highlight"><pre><span></span><span class="gp">...\&gt;</span> py manage.py startapp polls
</pre></div>
</section>
</div>
<p>That’ll create a directory <code class="file docutils literal notranslate"><span class="pre">polls</span></code>, which is laid out like this:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">polls</span><span class="o">/</span>
    <span class="fm">__init__</span><span class="o">.</span><span class="n">py</span>
    <span class="n">admin</span><span class="o">.</span><span class="n">py</span>
    <span class="n">apps</span><span class="o">.</span><span class="n">py</span>
    <span class="n">migrations</span><span class="o">/</span>
        <span class="fm">__init__</span><span class="o">.</span><span class="n">py</span>
    <span class="n">models</span><span class="o">.</span><span class="n">py</span>
    <span class="n">tests</span><span class="o">.</span><span class="n">py</span>
    <span class="n">views</span><span class="o">.</span><span class="n">py</span>
</pre></div>
</div>
<p>This directory structure will house the poll application.</p>
</div>
<div class="section" id="s-write-your-first-view">
<span id="write-your-first-view"></span><h2>Write your first view<a class="headerlink" href="#write-your-first-view" title="Permalink to this headline">¶</a></h2>
<p>Let’s write the first view. Open the file <code class="docutils literal notranslate"><span class="pre">polls/views.py</span></code>
and put the following Python code in it:</p>
<div class="literal-block-wrapper docutils container" id="id1">
<div class="code-block-caption"><span class="caption-text">polls/views.py</span><a class="headerlink" href="#id1" title="Permalink to this code">¶</a><span class="btn-clipboard" title="Copy this code"><i class="icon icon-clipboard"></i></span></div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">django.http</span> <span class="kn">import</span> <span class="n">HttpResponse</span>


<span class="k">def</span> <span class="nf">index</span><span class="p">(</span><span class="n">request</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">HttpResponse</span><span class="p">(</span><span class="s2">"Hello, world. You're at the polls index."</span><span class="p">)</span>
</pre></div>
</div>
</div>
<p>This is the simplest view possible in Django. To call the view, we need to map
it to a URL - and for this we need a URLconf.</p>
<p>To create a URLconf in the polls directory, create a file called <code class="docutils literal notranslate"><span class="pre">urls.py</span></code>.
Your app directory should now look like:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">polls</span><span class="o">/</span>
    <span class="fm">__init__</span><span class="o">.</span><span class="n">py</span>
    <span class="n">admin</span><span class="o">.</span><span class="n">py</span>
    <span class="n">apps</span><span class="o">.</span><span class="n">py</span>
    <span class="n">migrations</span><span class="o">/</span>
        <span class="fm">__init__</span><span class="o">.</span><span class="n">py</span>
    <span class="n">models</span><span class="o">.</span><span class="n">py</span>
    <span class="n">tests</span><span class="o">.</span><span class="n">py</span>
    <span class="n">urls</span><span class="o">.</span><span class="n">py</span>
    <span class="n">views</span><span class="o">.</span><span class="n">py</span>
</pre></div>
</div>
<p>In the <code class="docutils literal notranslate"><span class="pre">polls/urls.py</span></code> file include the following code:</p>
<div class="literal-block-wrapper docutils container" id="id2">
<div class="code-block-caption"><span class="caption-text">polls/urls.py</span><a class="headerlink" href="#id2" title="Permalink to this code">¶</a><span class="btn-clipboard" title="Copy this code"><i class="icon icon-clipboard"></i></span></div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">django.urls</span> <span class="kn">import</span> <span class="n">path</span>

<span class="kn">from</span> <span class="nn">.</span> <span class="kn">import</span> <span class="n">views</span>

<span class="n">urlpatterns</span> <span class="o">=</span> <span class="p">[</span>
    <span class="n">path</span><span class="p">(</span><span class="s1">''</span><span class="p">,</span> <span class="n">views</span><span class="o">.</span><span class="n">index</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s1">'index'</span><span class="p">),</span>
<span class="p">]</span>
</pre></div>
</div>
</div>
<p>The next step is to point the root URLconf at the <code class="docutils literal notranslate"><span class="pre">polls.urls</span></code> module. In
<code class="docutils literal notranslate"><span class="pre">mysite/urls.py</span></code>, add an import for <code class="docutils literal notranslate"><span class="pre">django.urls.include</span></code> and insert an
<a class="reference internal" href="https://docs.djangoproject.com/en/2.2/ref/urls/#django.urls.include" title="django.urls.include"><code class="xref py py-func docutils literal notranslate"><span class="pre">include()</span></code></a> in the <code class="docutils literal notranslate"><span class="pre">urlpatterns</span></code> list, so you have:</p>
<div class="literal-block-wrapper docutils container" id="id3">
<div class="code-block-caption"><span class="caption-text">mysite/urls.py</span><a class="headerlink" href="#id3" title="Permalink to this code">¶</a><span class="btn-clipboard" title="Copy this code"><i class="icon icon-clipboard"></i></span></div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">django.contrib</span> <span class="kn">import</span> <span class="n">admin</span>
<span class="kn">from</span> <span class="nn">django.urls</span> <span class="kn">import</span> <span class="n">include</span><span class="p">,</span> <span class="n">path</span>

<span class="n">urlpatterns</span> <span class="o">=</span> <span class="p">[</span>
    <span class="n">path</span><span class="p">(</span><span class="s1">'polls/'</span><span class="p">,</span> <span class="n">include</span><span class="p">(</span><span class="s1">'polls.urls'</span><span class="p">)),</span>
    <span class="n">path</span><span class="p">(</span><span class="s1">'admin/'</span><span class="p">,</span> <span class="n">admin</span><span class="o">.</span><span class="n">site</span><span class="o">.</span><span class="n">urls</span><span class="p">),</span>
<span class="p">]</span>
</pre></div>
</div>
</div>
<p>The <a class="reference internal" href="https://docs.djangoproject.com/en/2.2/ref/urls/#django.urls.include" title="django.urls.include"><code class="xref py py-func docutils literal notranslate"><span class="pre">include()</span></code></a> function allows referencing other URLconfs.
Whenever Django encounters <a class="reference internal" href="https://docs.djangoproject.com/en/2.2/ref/urls/#django.urls.include" title="django.urls.include"><code class="xref py py-func docutils literal notranslate"><span class="pre">include()</span></code></a>, it chops off whatever
part of the URL matched up to that point and sends the remaining string to the
included URLconf for further processing.</p>
<p>The idea behind <a class="reference internal" href="https://docs.djangoproject.com/en/2.2/ref/urls/#django.urls.include" title="django.urls.include"><code class="xref py py-func docutils literal notranslate"><span class="pre">include()</span></code></a> is to make it easy to
plug-and-play URLs. Since polls are in their own URLconf
(<code class="docutils literal notranslate"><span class="pre">polls/urls.py</span></code>), they can be placed under “/polls/”, or under
“/fun_polls/”, or under “/content/polls/”, or any other path root, and the
app will still work.</p>
<div class="admonition-when-to-use-func-django-urls-include admonition">
<p class="first admonition-title">When to use <a class="reference internal" href="https://docs.djangoproject.com/en/2.2/ref/urls/#django.urls.include" title="django.urls.include"><code class="xref py py-func docutils literal notranslate"><span class="pre">include()</span></code></a></p>
<p class="last">You should always use <code class="docutils literal notranslate"><span class="pre">include()</span></code> when you include other URL patterns.
<code class="docutils literal notranslate"><span class="pre">admin.site.urls</span></code> is the only exception to this.</p>
</div>
<p>You have now wired an <code class="docutils literal notranslate"><span class="pre">index</span></code> view into the URLconf. Verify it’s working with
the following command:</p>
<div class="console-block" id="console-block-6">
<input class="c-tab-unix" id="c-tab-6-unix" type="radio" name="console-6" checked="checked">
<label for="c-tab-6-unix" title="Linux/macOS">/</label>
<input class="c-tab-win" id="c-tab-6-win" type="radio" name="console-6">
<label for="c-tab-6-win" title="Windows"></label>
<section class="c-content-unix" id="c-content-6-unix">
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$</span> python manage.py runserver
</pre></div>
</div>
</section>
<section class="c-content-win" id="c-content-6-win">
<div class="highlight"><pre><span></span><span class="gp">...\&gt;</span> py manage.py runserver
</pre></div>
</section>
</div>
<p>Go to <a class="reference external" href="http://localhost:8000/polls/">http://localhost:8000/polls/</a> in your browser, and you should see the
text “<em>Hello, world. You’re at the polls index.</em>”, which you defined in the
<code class="docutils literal notranslate"><span class="pre">index</span></code> view.</p>
<div class="admonition-page-not-found admonition">
<p class="first admonition-title">Page not found?</p>
<p class="last">If you get an error page here, check that you’re going to
<a class="reference external" href="http://localhost:8000/polls/">http://localhost:8000/polls/</a> and not <a class="reference external" href="http://localhost:8000/">http://localhost:8000/</a>.</p>
</div>
<p>The <a class="reference internal" href="https://docs.djangoproject.com/en/2.2/ref/urls/#django.urls.path" title="django.urls.path"><code class="xref py py-func docutils literal notranslate"><span class="pre">path()</span></code></a> function is passed four arguments, two required:
<code class="docutils literal notranslate"><span class="pre">route</span></code> and <code class="docutils literal notranslate"><span class="pre">view</span></code>, and two optional: <code class="docutils literal notranslate"><span class="pre">kwargs</span></code>, and <code class="docutils literal notranslate"><span class="pre">name</span></code>.
At this point, it’s worth reviewing what these arguments are for.</p>
<div class="section" id="s-path-argument-route">
<span id="path-argument-route"></span><h3><a class="reference internal" href="https://docs.djangoproject.com/en/2.2/ref/urls/#django.urls.path" title="django.urls.path"><code class="xref py py-func docutils literal notranslate"><span class="pre">path()</span></code></a> argument: <code class="docutils literal notranslate"><span class="pre">route</span></code><a class="headerlink" href="#path-argument-route" title="Permalink to this headline">¶</a></h3>
<p><code class="docutils literal notranslate"><span class="pre">route</span></code> is a string that contains a URL pattern. When processing a request,
Django starts at the first pattern in <code class="docutils literal notranslate"><span class="pre">urlpatterns</span></code> and makes its way down
the list, comparing the requested URL against each pattern until it finds one
that matches.</p>
<p>Patterns don’t search GET and POST parameters, or the domain name. For example,
in a request to <code class="docutils literal notranslate"><span class="pre">https://www.example.com/myapp/</span></code>, the URLconf will look for
<code class="docutils literal notranslate"><span class="pre">myapp/</span></code>. In a request to <code class="docutils literal notranslate"><span class="pre">https://www.example.com/myapp/?page=3</span></code>, the
URLconf will also look for <code class="docutils literal notranslate"><span class="pre">myapp/</span></code>.</p>
</div>
<div class="section" id="s-path-argument-view">
<span id="path-argument-view"></span><h3><a class="reference internal" href="https://docs.djangoproject.com/en/2.2/ref/urls/#django.urls.path" title="django.urls.path"><code class="xref py py-func docutils literal notranslate"><span class="pre">path()</span></code></a> argument: <code class="docutils literal notranslate"><span class="pre">view</span></code><a class="headerlink" href="#path-argument-view" title="Permalink to this headline">¶</a></h3>
<p>When Django finds a matching pattern, it calls the specified view function with
an <a class="reference internal" href="https://docs.djangoproject.com/en/2.2/ref/request-response/#django.http.HttpRequest" title="django.http.HttpRequest"><code class="xref py py-class docutils literal notranslate"><span class="pre">HttpRequest</span></code></a> object as the first argument and any
“captured” values from the route as keyword arguments. We’ll give an example
of this in a bit.</p>
</div>
<div class="section" id="s-path-argument-kwargs">
<span id="path-argument-kwargs"></span><h3><a class="reference internal" href="https://docs.djangoproject.com/en/2.2/ref/urls/#django.urls.path" title="django.urls.path"><code class="xref py py-func docutils literal notranslate"><span class="pre">path()</span></code></a> argument: <code class="docutils literal notranslate"><span class="pre">kwargs</span></code><a class="headerlink" href="#path-argument-kwargs" title="Permalink to this headline">¶</a></h3>
<p>Arbitrary keyword arguments can be passed in a dictionary to the target view. We
aren’t going to use this feature of Django in the tutorial.</p>
</div>
<div class="section" id="s-path-argument-name">
<span id="path-argument-name"></span><h3><a class="reference internal" href="https://docs.djangoproject.com/en/2.2/ref/urls/#django.urls.path" title="django.urls.path"><code class="xref py py-func docutils literal notranslate"><span class="pre">path()</span></code></a> argument: <code class="docutils literal notranslate"><span class="pre">name</span></code><a class="headerlink" href="#path-argument-name" title="Permalink to this headline">¶</a></h3>
<p>Naming your URL lets you refer to it unambiguously from elsewhere in Django,
especially from within templates. This powerful feature allows you to make
global changes to the URL patterns of your project while only touching a single
file.</p>
<p>When you’re comfortable with the basic request and response flow, read
<a class="reference internal" href="https://docs.djangoproject.com/en/2.2/intro/tutorial02/"><span class="doc">part 2 of this tutorial</span></a> to start working with the
database.</p>
</div>
</div>
</div>

</div>



<div class="browse-horizontal">
  
  <div class="left"><a href="https://docs.djangoproject.com/en/2.2/intro/install/"><i class="icon icon-chevron-left"></i> Quick install guide</a></div>
  
  
  <div class="right"><a href="https://docs.djangoproject.com/en/2.2/intro/tutorial02/">Writing your first Django app, part 2 <i class="icon icon-chevron-right"></i></a></div>
  
</div>



        <a href="#top" class="backtotop"><i class="icon icon-chevron-up"></i> Back to Top</a>
      </div>

      
<h1 class="visuallyhidden">Additional Information</h1>
<div role="complementary">
  
  

<form action="https://docs.djangoproject.com/en/2.2/search/" class="search form-input" role="search">
  <label class="visuallyhidden" for="id_q">Search:</label>
    <input type="search" name="q" id="id_q" placeholder="Search 2.2 documentation">

    <button type="submit">
      <i class="icon icon-search"></i>
      <span class="visuallyhidden">Search</span>
    </button>
</form>

  

  


  <div class="fundraising-sidebar">
    <h2>Support Django!</h2>

    <div class="small-heart">
      <img src="urls_files/small-fundraising-heart.png" alt="Support Django!">
    </div>

    <div class="small-cta">
      <ul class="list-links-small">
        <li><a href="https://www.djangoproject.com/fundraising/">
          Phillip Stromberg donated to the Django Software Foundation to
          support Django development. Donate today!
        </a></li>
      </ul>
    </div>
  </div>



  
    <h2>Contents</h2>
    
    <ul>
<li><a class="reference internal" href="#">Writing your first Django app, part 1</a><ul>
<li><a class="reference internal" href="#creating-a-project">Creating a project</a></li>
<li><a class="reference internal" href="#the-development-server">The development server</a></li>
<li><a class="reference internal" href="#creating-the-polls-app">Creating the Polls app</a></li>
<li><a class="reference internal" href="#write-your-first-view">Write your first view</a><ul>
<li><a class="reference internal" href="#path-argument-route"><code class="docutils literal notranslate"><span class="pre">path()</span></code> argument: <code class="docutils literal notranslate"><span class="pre">route</span></code></a></li>
<li><a class="reference internal" href="#path-argument-view"><code class="docutils literal notranslate"><span class="pre">path()</span></code> argument: <code class="docutils literal notranslate"><span class="pre">view</span></code></a></li>
<li><a class="reference internal" href="#path-argument-kwargs"><code class="docutils literal notranslate"><span class="pre">path()</span></code> argument: <code class="docutils literal notranslate"><span class="pre">kwargs</span></code></a></li>
<li><a class="reference internal" href="#path-argument-name"><code class="docutils literal notranslate"><span class="pre">path()</span></code> argument: <code class="docutils literal notranslate"><span class="pre">name</span></code></a></li>
</ul>
</li>
</ul>
</li>
</ul>

    
  

  
  <h2>Browse</h2>
  <ul>
    
    
    <li>Prev: <a href="https://docs.djangoproject.com/en/2.2/intro/install/">Quick install guide</a></li>
    
    
    <li>Next: <a href="https://docs.djangoproject.com/en/2.2/intro/tutorial02/">Writing your first Django app, part 2</a></li>
    
    <li><a href="https://docs.djangoproject.com/en/2.2/contents/">Table of contents</a></li>
    
    <li><a href="https://docs.djangoproject.com/en/2.2/genindex/">General Index</a></li>
    
    <li><a href="https://docs.djangoproject.com/en/2.2/py-modindex/">Python Module Index</a></li>
    
    
  </ul>
  

  
  <h2>You are here:</h2>
  <ul>
    <li>
      <a href="https://docs.djangoproject.com/en/2.2/">Django 2.2 documentation</a>
      
      <ul><li><a href="https://docs.djangoproject.com/en/2.2/intro/">Getting started</a>
      
      <ul><li>Writing your first Django app, part 1</li></ul>
      </li></ul>
    </li>
  </ul>
  

  
  <h2 id="getting-help-sidebar">Getting help</h2>
  <dl class="list-links">
    <dt><a href="https://docs.djangoproject.com/en/2.2/faq/">FAQ</a></dt>
    <dd>Try the FAQ — it's got answers to many common questions.</dd>

    <dt><a href="https://docs.djangoproject.com/en/stable/genindex/">Index</a>, <a href="https://docs.djangoproject.com/en/stable/py-modindex/">Module Index</a>, or <a href="https://docs.djangoproject.com/en/stable/contents/">Table of Contents</a></dt>
    <dd>Handy when looking for specific information.</dd>

    <dt><a href="https://groups.google.com/group/django-users/">django-users mailing list</a></dt>
    <dd>Search for information in the archives of the django-users mailing list, or post a question.</dd>

    <dt><a href="irc://irc.freenode.net/django">#django IRC channel</a></dt>
    <dd>Ask a question in the #django IRC channel, or search the IRC logs to see if it’s been asked before.</dd>

    <dt><a href="https://code.djangoproject.com/">Ticket tracker</a></dt>
    <dd>Report bugs with Django or Django documentation in our ticket tracker.</dd>
  </dl>
  

  
  <h2>Download:</h2>
  <p>
    Offline (Django 2.2):
    <a href="https://media.djangoproject.com/docs/django-docs-2.2-en.zip">HTML</a> |
    <a href="https://media.readthedocs.org/pdf/django/2.2.x/django.pdf">PDF</a> |
    <a href="https://media.readthedocs.org/epub/django/2.2.x/django.epub">ePub</a>
    <br>
    <span class="quiet">
      Provided by <a href="https://readthedocs.org/">Read the Docs</a>.
    </span>
  </p>
  
</div>

      

    </div>

     
     

    
    
    

    
      
<div role="contentinfo">
  <div class="subfooter">
    <div class="container">
      <h1 class="visuallyhidden">Django Links</h1>

      <div class="col learn">
        <h2>Learn More</h2>
        <ul>
          <li><a href="https://www.djangoproject.com/start/overview/">About Django</a></li>
          
          <li><a href="https://www.djangoproject.com/start/">Getting Started with Django</a></li>
          <li><a href="https://docs.djangoproject.com/en/dev/internals/organization/">Team Organization</a></li>
          <li><a href="https://www.djangoproject.com/foundation/">Django Software Foundation</a></li>
          <li><a href="https://www.djangoproject.com/conduct/">Code of Conduct</a></li>
          <li><a href="https://www.djangoproject.com/diversity/">Diversity Statement</a></li>
        </ul>
      </div>

      <div class="col involved">
        <h2>Get Involved</h2>
        <ul>
          <li><a href="https://www.djangoproject.com/community/">Join a Group</a></li>
          <li><a href="https://docs.djangoproject.com/en/dev/internals/contributing/">Contribute to Django</a></li>
          <li><a href="https://docs.djangoproject.com/en/dev/internals/contributing/bugs-and-features/">Submit a Bug</a></li>
          <li><a href="https://docs.djangoproject.com/en/dev/internals/security/#reporting-security-issues">Report a Security Issue</a></li>
        </ul>
      </div>

      <div class="col follow last-child">
        <h2>Follow Us</h2>
        <ul>
          <li><a href="https://github.com/django">GitHub</a></li>
          <li><a href="https://twitter.com/djangoproject">Twitter</a></li>
          <li><a href="https://www.djangoproject.com/rss/weblog/">News RSS</a></li>
          <li><a href="https://groups.google.com/forum/#!forum/django-users">Django Users Mailing List</a></li>
        </ul>
      </div>

    </div>
  </div>

  <div class="footer">
    <div class="container">
      <div class="footer-logo">
        <a class="logo" href="https://www.djangoproject.com/">Django</a>
      </div>
      <ul class="thanks">
        <li>
          <span>Hosting by</span> <a class="rackspace" href="https://www.rackspace.com/">Rackspace</a>
        </li>
        <li class="design"><span>Design by</span> <a class="threespot" href="https://www.threespot.com/">Threespot</a> <span class="ampersand">&amp;</span> <a class="andrevv" href="http://andrevv.com/"></a></li>
      </ul>
      <p class="copyright">© 2005-2019
        <a href="https://www.djangoproject.com/foundation/"> Django Software
        Foundation</a> and individual contributors. Django is a
        <a href="https://www.djangoproject.com/trademarks/">registered
        trademark</a> of the Django Software Foundation.
      </p>
    </div>
  </div>

</div>

    

    
    <script>
    function extless(input) {
        return input.replace(/(.*)\.[^.]+$/, '$1');
    }
    var require = {
        shim: {
            'jquery': [],
            'jquery.inview': ["jquery"],
            'jquery.payment': ["jquery"],
            'jquery.flot': ["jquery"],
            'jquery.unveil': ["jquery"],
            'stripe': {
              exports: 'Stripe'
            }
        },
        paths: {
            "jquery": extless("https://static.djangoproject.com/js/lib/jquery/dist/jquery.min.87e69028f78d.js"),
            "jquery.inview": extless("https://static.djangoproject.com/js/lib/jquery.inview/jquery.inview.min.4edba1c65592.js"),
            "jquery.payment": extless("https://static.djangoproject.com/js/lib/jquery.payment/lib/jquery.payment.e99c05ca79ae.js"),
            "jquery.unveil": extless("https://static.djangoproject.com/js/lib/unveil/jquery.unveil.min.ac79eb277093.js"),
            "jquery.flot": extless("https://static.djangoproject.com/js/lib/jquery-flot/jquery.flot.min.9964206e9d7f.js"),
            "clipboard": extless("https://static.djangoproject.com/js/lib/clipboard/dist/clipboard.min.bd70fd596a23.js"),
            "mod/floating-warning": extless("https://static.djangoproject.com/js/mod/floating-warning.a21b2abd2884.js"),
            "mod/list-collapsing": extless("https://static.djangoproject.com/js/mod/list-collapsing.c1a08d3ef9e9.js"),
            "mod/list-feature": extless("https://static.djangoproject.com/js/mod/list-feature.73529480f25b.js"),
            "mod/mobile-menu": extless("https://static.djangoproject.com/js/mod/mobile-menu.841726ee903a.js"),
            "mod/version-switcher": extless("https://static.djangoproject.com/js/mod/version-switcher.c28bb83972bb.js"),
            "mod/search-key": extless("https://static.djangoproject.com/js/mod/search-key.f3c0a6fcfedd.js"),
            "mod/stripe-custom-checkout": extless("https://static.djangoproject.com/js/mod/stripe-custom-checkout.aac1352045b7.js"),
            "mod/stripe-change-card": extless("https://static.djangoproject.com/js/mod/stripe-change-card.682c710317a8.js"),
            "mod/console-tabs": extless("https://static.djangoproject.com/js/mod/console-tabs.70ce882faaf3.js"),
            "stripe-checkout": "https://checkout.stripe.com/checkout",
            "stripe": "https://js.stripe.com/v2/?"  // ? needed due to require.js
        }
    };
    </script>
    <script data-main="https://static.djangoproject.com/js/main.07884ebc4865.js" src="urls_files/require.js"></script>
    



  

</body></html>