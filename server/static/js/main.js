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
    var snippet = '';
    snippet = snippet + '<div>Name: ' + result.name + '</div>';
    snippet = snippet + '<div>Round: ' + result.round + '</div>';
    
    snippet = snippet + '<div>Draw: ' + result.cardsToDraw + ' / Play:' + result.cardsToPlay + '</div>';
    $('#gameinfo').empty();
    $('#gameinfo').prepend(snippet);

    if (result.goal) {
      $('#goalStack').append('<div class="smallcard draggable" id="' + result.goal.id + '"><img class="smallimg" src="/static/pics/cards/goals/' + result.goal.id + '.png" /></div>')
    }
      
    for (var i = 0; i < result.field._cards.length; i++) {
      var c = result.field._cards[i];
      $('#field').append('<div class="smallcard draggable" id="' + c.id + '"><img class="smallimg" src="/static/pics/cards/' + c.category + 's/' + c.id + '.png" /></div>')
    }

    for (var i = 0; i < result.hand._cards.length; i++) {
      var c = result.hand._cards[i];
      $('#hand').append('<div class="smallcard draggable" id="' + c.id + '"><img class="smallimg" src="/static/pics/cards/' + c.category + 's/' + c.id + '.png" /></div>')
    }
    init();
  });
  
}