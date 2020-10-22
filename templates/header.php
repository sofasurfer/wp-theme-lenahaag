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


        <link rel="apple-touch-icon" sizes="57x57" href="<?= get_stylesheet_directory_uri(); ?>/assets/images/ico/apple-icon-57x57.png">
        <link rel="apple-touch-icon" sizes="60x60" href="<?= get_stylesheet_directory_uri(); ?>/assets/images/ico/apple-icon-60x60.png">
        <link rel="apple-touch-icon" sizes="72x72" href="<?= get_stylesheet_directory_uri(); ?>/assets/images/ico/apple-icon-72x72.png">
        <link rel="apple-touch-icon" sizes="76x76" href="<?= get_stylesheet_directory_uri(); ?>/assets/images/ico/apple-icon-76x76.png">
        <link rel="apple-touch-icon" sizes="114x114" href="<?= get_stylesheet_directory_uri(); ?>/assets/images/ico/apple-icon-114x114.png">
        <link rel="apple-touch-icon" sizes="120x120" href="<?= get_stylesheet_directory_uri(); ?>/assets/images/ico/apple-icon-120x120.png">
        <link rel="apple-touch-icon" sizes="144x144" href="<?= get_stylesheet_directory_uri(); ?>/assets/images/ico/apple-icon-144x144.png">
        <link rel="apple-touch-icon" sizes="152x152" href="<?= get_stylesheet_directory_uri(); ?>/assets/images/ico/apple-icon-152x152.png">
        <link rel="apple-touch-icon" sizes="180x180" href="<?= get_stylesheet_directory_uri(); ?>/assets/images/ico/apple-icon-180x180.png">
        <link rel="icon" type="image/png" sizes="192x192"  href="<?= get_stylesheet_directory_uri(); ?>/assets/images/ico/android-icon-192x192.png">
        <link rel="icon" type="image/png" sizes="32x32" href="<?= get_stylesheet_directory_uri(); ?>/assets/images/ico/favicon-32x32.png">
        <link rel="icon" type="image/png" sizes="96x96" href="<?= get_stylesheet_directory_uri(); ?>/assets/images/ico/favicon-96x96.png">
        <link rel="icon" type="image/png" sizes="16x16" href="<?= get_stylesheet_directory_uri(); ?>/assets/images/ico/favicon-16x16.png">
        <link rel="manifest" href="/manifest.json">
        <meta name="msapplication-TileColor" content="#ffffff">
        <meta name="msapplication-TileImage" content="/ms-icon-144x144.png">
        <meta name="theme-color" content="#ffffff">


        <script src="https://kit.fontawesome.com/c8df374f5c.js" crossorigin="anonymous"></script>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" />
        <link rel="stylesheet" href="<?= get_stylesheet_directory_uri(); ?>/style.css?v=1.1.0" />


    </head>
    <body>
    <div id="intro-screen">
        <div class="intro-screen-text"><img src="https://www.einepraxis.ch/wp-content/uploads/2020/10/LOGO_HOMEPAGE.svg" /></div>
    </div>
    <div id="home"></div>
    <div class="header-nav d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white ">

      <h5 id="m-open" class="my-0 mr-md-auto font-weight-normal"><a href="#home"><?= get_bloginfo(); ?></a></h5>
      <input id="m-nav" type="checkbox"  />
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
            $image_mobile = get_field('rev_header_image_mobile');
        ?>
        <img srcset="<?= $image['url'];?> 2048w, 
                <?= $image_mobile['url'];?> 300w, 
                <?= $image_mobile['url'];?> 1024w, 
                <?= $image_mobile['url'];?> 768w, 
                <?= $image['url'];?> 1536w" 
                 class="wp-image-64" src="<?= $image['url'];?>">
    </figure>

    <h1><?=  get_field('rev_header_headline'); ?></h1>
