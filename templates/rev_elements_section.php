<hr class="wp-block-separator is-style-wide">
<?php if($site_element['rev_elements_section_largeimage']): ?>
<div class="capture-image">
<img class="img-responsive" src="<?= $site_element['rev_elements_section_image']['url'];?>" />
</div>
<?php else: ?>
<div class="capture <?= ($site_element['rev_elements_section_paralax']) ? 'paralax' : '';?>" style="background-image: url('<?= $site_element['rev_elements_section_image']['url'];?>');"></div>
<?php endif; ?>
<a id="<?= $site_element['rev_elements_section_anchor'];?>" class="anchor"></a>
<h2><?= $site_element['rev_elements_section_title']; ?></h2>