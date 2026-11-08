(function () {
  'use strict';
  var avatar = document.getElementById('rotating-cat-avatar');
  if (!avatar) return;
  var original = avatar.getAttribute('src');
  var alternatives = avatar.getAttribute('data-cat-photos');
  if (!original || !alternatives) return;
  var photos = [original].concat(alternatives.split('|'));
  var storageKey = 'lastCatAvatar';
  var previous = 0;
  try {
    var saved = sessionStorage.getItem(storageKey);
    if (saved !== null && /^[0-9]+$/.test(saved) && Number(saved) < photos.length) {
      previous = Number(saved);
    }
  } catch (error) {}

  /* Exclude the last displayed photo; first-time visitors get a new portrait. */
  var choice = Math.floor(Math.random() * (photos.length - 1));
  if (choice >= previous) choice += 1;

  function remember(index, status) {
    avatar.setAttribute('data-cat-choice', String(index));
    avatar.setAttribute('data-cat-status', status);
    try { sessionStorage.setItem(storageKey, String(index)); } catch (error) {}
  }

  function restoreOriginal() {
    avatar.onload = null;
    avatar.onerror = null;
    avatar.src = original;
    remember(0, 'fallback');
  }

  if (choice === 0) {
    remember(0, 'ready');
    return;
  }

  /* Keep the original visible until the chosen image has decoded successfully. */
  var next = new Image();
  next.onerror = restoreOriginal;
  next.onload = function () {
    if (!next.naturalWidth || !next.naturalHeight) {
      restoreOriginal();
      return;
    }
    avatar.onerror = restoreOriginal;
    avatar.onload = function () {
      avatar.onload = null;
      remember(choice, 'ready');
    };
    avatar.src = next.src;
  };
  next.src = photos[choice];
})();
