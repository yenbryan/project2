$( document ).ready(function() {
    var last_selected = '#initial-category';
    $( ".category-select" ).click(function() {
        var selected = '#list-'+ $(this).attr('id');
        $(last_selected).hide();
        last_selected=selected;
        $(selected).show();
//        var url = '/'
//        $.ajax({
//            url: '/all_pokemon',
//            type: "GET",
//            success: function(data) {
//                $('body').append(data[0].fields.name);
//                console.log(data);
//            }
//        });
    });
    $( "#about-me-edit" ).click(function() {
        $('.panel-edit-form').show()
        $('.panel-info').hide()
        $( "#about-me-done").show()
        $( "#about-me-edit").hide()
    });

    $( "#about-me-done" ).click(function() {

//        var postData = {
//            "post":''
//        };

//        $.ajax({
//            url: '/profile/ajax-about-me-update',
//            type: 'POST',
//            dataType: 'json',
//            data: pokemonData,
//            success: function(response) {
//                console.log(response)
//            },
//            error: function(response) {
//                console.log(response)
//            }
//        });
        $('.panel-edit-form').hide()
        $('.panel-info').show()
        $( "#about-me-done").hide()
        $( "#about-me-edit").show()
    });

        $( "#profile-edit" ).click(function() {
        $('#profile-edit-form').show()
        $('#profile-info').hide()
        $( "#profile-done").show()
        $( "#profile-edit").hide()
    });

    $( "#profile-done" ).click(function() {
        $('#profile-edit-form').hide()
        $('#profile-info').show()
        $( "#profile-done").hide()
        $( "#profile-edit").show()
    });
    //$('#topwrapper').followTo(100);
});

    $(window).scroll(function(){
        $("#topwrapper").css("top",Math.max(0,50-$(this).scrollTop()));
    });

//var pokemonData = {
//    pokedex_id: 25,
//    image: "/media/img/25.png",
//    name: "Pikachu",
//    team: {
//        name: "dream team",
//        id: 1
//    }
//}
//
//pokemonData = JSON.stringify(pokemonData);