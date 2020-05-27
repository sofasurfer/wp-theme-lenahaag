<?php


if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly.
}



function c_shortcode_version(){
    $my_theme = wp_get_theme( 'revisia' );
    if ( $my_theme->exists() ){
        return $my_theme->get( 'Version' );
    }
    return 1.0;
}
add_shortcode( 'wp_version', 'c_shortcode_version' );



function c_register_maim_menu() {
  register_nav_menu('header-menu',__( 'Header Menu' ));
}
add_action( 'init', 'c_register_maim_menu' );

function c_remove_gutenberg() {
        remove_post_type_support( 'page', 'editor' );
        remove_post_type_support( 'post', 'editor' );
        remove_post_type_support( 'people', 'editor' );
}
add_action( 'init', 'c_remove_gutenberg' );

function writy_setup() {
    add_theme_support( 'align-wide' );
    add_theme_support( 'wp-block-styles' );
}
add_action( 'after_setup_theme', 'writy_setup' );


function cc_mime_types($mimes = [] ){
    $mimes['svg'] = 'image/svg+xml';
    return $mimes;
}
add_filter('upload_mimes', 'cc_mime_types' );


/*
    Adds custom CSS to admin
*/
function my_custom_admin_css() {
    echo '<style>
    [data-layout="rev_elements_section"] .acf-fc-layout-handle{
        color: white!important;
        background-color: #0073aa;
    }
    </style>';
}
add_action('admin_head', 'my_custom_admin_css');
