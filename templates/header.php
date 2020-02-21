<!DOCTYPE html>
<html  <?php language_attributes(); ?> >
    <head>
        <meta charset="utf-8">
        <title><?php wp_title( '|', true, 'right' ); ?><?= get_bloginfo(); ?></title>
        <meta name="author" content="SofaSurfer.org">
        <meta name="description" content="<?= get_bloginfo('description'); ?>">


        <!-- Preventing IE11 to request by default the /browserconfig.xml more than one time -->
        <meta name="msapplication-config" content="none">
        <!-- Disable touch highlighting in IE -->
        <meta name="msapplication-tap-highlight" content="no">
        <!-- Ensure edge compatibility in IE (HTTP header can be set in web server config) -->
        <meta http-equiv="X-UA-Compatible" content="IE=edge, chrome=1">
        <!-- Force viewport width and pixel density. Plus, disable shrinking. -->
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <!-- Disable Skype browser-plugin -->
        <meta name="SKYPE_TOOLBAR" content="SKYPE_TOOLBAR_PARSER_COMPATIBLE">

        <script src="https://kit.fontawesome.com/c8df374f5c.js" crossorigin="anonymous"></script>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" />
        <link rel="stylesheet" href="<?= get_stylesheet_directory_uri(); ?>/style.css?v=<?= do_shortcode('[wp_version]') ;?>" />

    </head>
    <body>
    <!--div id="intro-screen">
        <div class="intro-screen-text"><?= get_bloginfo(); ?></div>
    </div-->
    <div id="home"></div>
    <div class="header-nav d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white ">

      <h5 class="my-0 mr-md-auto font-weight-normal"><a href="#home"><?= get_bloginfo(); ?></a></h5>
        <!-- The WordPress Menu goes here -->
        <nav id="navbar-example2">
        <?php wp_nav_menu( 
            array( 
                'theme_location'    => 'header-menu',
                'container'         => false,
                'menu_class'        => 'my-2 my-md-0 mr-md-3',
            )
        ); ?>
        </nav>
      <!--a class="btn btn-outline-primary" href="tel:0792428243">Termin: 079 242 82 43</a-->
    </div>

    <div id="main" class="container-fluid" data-spy="scroll" data-target="#navbar-example2" data-offset="0">
      
    <figure class="wp-block-image alignfull img-fluid-header">
        <?php
            $image = get_field('rev_header_image');
        ?>
        <img src="<?= $image['url']; ?>" alt="" class="wp-image-64" />
    </figure>

    <h1><?=  get_field('rev_header_headline'); ?></h1>
