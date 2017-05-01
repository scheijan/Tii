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


function flip() {
  $('.smallcard').toggleClass('flipped');
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
    
    snippet = snippet + '<div>Draw: ' + result.gameData.cardsToDraw + ' / Play:' + result.gameData.cardsToPlay + '</div>';
    
    $('#gameinfo').html(snippet);
    $('#gameinfo').append('<button onclick="flip()">flip</button>');

    if (result.goal) {
      $('#goalStack').html(createCard(result.goal));
    }

    $('#rules').empty();
    $('#rules').append('<div class="label">Rules</div>');
    for (var i = 0; i < result.rules._cards.length; i++) {
      var c = result.rules._cards[i];
      $('#rules').append(createCard(c))
    }
      
    $('#field').empty();
    $('#field').append('<div class="label">Field</div>');
    for (var i = 0; i < result.field._cards.length; i++) {
      var c = result.field._cards[i];
      $('#field').append(createCard(c))
    }

    $('#hand').empty();
    $('#hand').append('<div class="label">Hand</div>');
    for (var i = 0; i < result.hand._cards.length; i++) {
      var c = result.hand._cards[i];
      $('#hand').append(createCard(c));
    }
    init();
  });
}


function createCard(card) {
  if (card.category === 'rule') {
    return '<div class="smallcard draggable" id="' + card.id + '">\
              <div class="front">\
                <div class="textcard">' + card.name + '</div>\
              </div>\
              <div class="back textcardback">\
                <img class="card textcardback" src="/static/pics/card.png"/>\
              </div>\
            </div>'
  } else if (card.category === 'goal') {
    return '<div class="smallcard draggable" id="' + card.id + '">\
              <div class="front">\
                <img class="smallimg" src="/static/pics/cards/' + card.category + 's/' + card.id + '.png" />\
              </div>\
              <div class="back goalcardback card"><br/><b>' + card.name + '</b><br/><br/>' + card.description + '</div>\
            </div>'
  } else {
    return '<div class="smallcard draggable" id="' + card.id + '">\
               <div class="front">\
                <img class="smallimg" src="/static/pics/cards/' + card.category + 's/' + card.id + '.png" />\
              </div>\
              <div class="back">\
                <img class="card" src="/static/pics/card.png"/>\
              </div>\
            </div>'
  }
}