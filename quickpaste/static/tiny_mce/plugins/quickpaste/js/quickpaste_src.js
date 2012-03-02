(function($){
    $(document).ready(function() {
        $('#id_upload').uploadify({
            'auto': true,
            'fileDataName': 'upload',
            'uploader':     url_tinymce + 'plugins/quickpaste/js/uploadify/uploadify.swf',
            'script':       url_upload,
            'cancelImg':    url_tinymce + 'plugins/quickpaste/js/uploadify/cancel.png',
            'buttonImg':    url_button,
            'scriptData'  : {session_key: session_key},
            'onComplete': function(event, ID, fileObj, response, data) {
                QuickPasteDialog.insert(response);
            }
        });
    });
})(jQuery);
