$( init );
 
function init() {
  $('.draggable').draggable({
      // containment: '#content',
      cursor: 'move',
      stack: '.draggable',
      revert: true
  });

  $('.droppable').droppable({
      hoverClass: 'hovered',
      drop: handleDropEvent,
      accept: '.draggable',
    });
}

function handleDropEvent( event, ui ) {
  var draggable = ui.draggable;
  draggable.position( { of: $(this), my: 'left top', at: 'left top' } );
  draggable.draggable( 'option', 'revert', false );
  console.log( 'the card with ID "' + draggable.attr('id') + '" was dropped onto me!' );
}

function getData(n) {
  $.getJSON("/state?n=" + n, function(result){
    var snippet = '<div class="gameinfo">';
    snippet = snippet + '<div>Name: ' + result.name + '</div>';
    snippet = snippet + '<div>Round: ' + result.round + '</div>';
    snippet = snippet + '<div>Draw: ' + result.cardsToDraw + ' / Play:' + result.cardsToPlay + '</div>';
    snippet = snippet + '</div>'
    $('#board').prepend(snippet)

    
    for (var i = 0; i < result.deck._cards.length; i++) {
      var c = result.deck._cards[i];
      $('#deck').append('<div class="smallcard draggable" id="' + c.id + '"><img class="smallimg" src="/static/pics/cards/' + c.category + 's/' + c.id + '.png" /></div>')
    }

    for (var i = 0; i < result.hand._cards.length; i++) {
      var c = result.hand._cards[i];
      $('#hand').append('<div class="smallcard draggable" id="' + c.id + '"><img class="smallimg" src="/static/pics/cards/' + c.category + 's/' + c.id + '.png" /></div>')
    }
    init();
  });
  
}