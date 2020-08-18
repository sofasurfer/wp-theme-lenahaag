    <!--footer class="footer">
        <div class="container-fluid">
            <ul>
                <li><a href="tel:0792428243"><i class="fas fa-phone"></i></a></li>
                <li><a href="mailto:info@einepraxis.ch"><i class="fas fa-envelope-open-text"></i></a></li>
            </ul>
        </div>
    </footer-->

    <script src="https://cdn.jsdelivr.net/npm/vanilla-lazyload@12.0.0/dist/lazyload.min.js"></script>
    <script
              src="https://code.jquery.com/jquery-3.4.1.min.js"
              integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo="
              crossorigin="anonymous"></script>

    <script>

        $( document ).ready(function() {

            // Hide intro
            setTimeout(function(){
                $('#intro-screen').fadeOut( "slow", function() {
                    $(this).remove();
                });
            }, 3000);

            $('#intro-screen').click(function(){
                $(this).fadeOut( "slow", function() {
                    $(this).remove();
                });
            });
        });

        /*
            Fix anchor
        */
        $( 'body' ).scroll(function() {
            setTimeout(function(){
                var scrollDistance = $(window).scrollTop();

                // Assign active class to nav links while scolling
                $('a.anchor').each(function(i) {

                    var anchor = '#' + $(this).attr('id');
                    if ($(this).position().top <= scrollDistance + 200 ) {
                        $('#menu-menu-1').find('a').removeClass('active');
                        $('#menu-menu-1 a').each(function(){
                            console.log( anchor + '/' + $(this).attr('href') );
                            if( $(this).attr('href') == anchor ){

                                $(this).addClass('active');
                            }
                        });
                    }                
                });
            }, 500);
        });

    </script>


</body>
</html>