/******/ (() => { // webpackBootstrap
/******/ 	"use strict";
/*!*************************************************************!*\
  !*** ../demo5/src/js/pages/custom/contacts/edit-contact.js ***!
  \*************************************************************/


// Class definition
var KTContactsEdit = function () {
	// Base elements
	var avatar;

	var initAvatar = function() {
		avatar = new KTImageInput('kt_contacts_edit_avatar');
	}

	return {
		// public functions
		init: function() {
			initAvatar();
		}
	};
}();

jQuery(document).ready(function() {
	KTContactsEdit.init();
});

/******/ })()
;
//# sourceMappingURL=edit-contact.js.map