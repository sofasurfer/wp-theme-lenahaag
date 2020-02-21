<?php
// Set post
if( have_posts() ) the_post();

$page_id = get_queried_object_id();

get_template_part('templates/header');


// Get Site Elements
$site_elements = get_field('rev_elements',$page_id);
if( !empty($site_elements)){
    foreach( $site_elements as $site_element ){
        include( locate_template( 'templates/' . $site_element['acf_fc_layout'] . '.php', false, false ) );
    }
}


get_template_part('templates/footer');

?>