(function ( $, window, document, undefined ) {
    
    // Create the defaults once
    var pluginName = 'client_selector',
        defaults = {
            callback:function(user){} // jshint ignore: line
        };

    // The actual plugin constructor
    function Plugin( element, options ) 
    {
        this.element = element;

        this.options = $.extend( {}, defaults, options);
        this.element.callback = this.options.callback;
        
        this._defaults = defaults;
        this._name = pluginName;
        
        this.init();
    }

    Plugin.prototype.init = function () 
    {
        // Place initialization logic here
        // You already have access to the DOM element and
        // the options via the instance, e.g. this.element 
        // and this.options

        this.element.callback( this.o );
    };

    // A really lightweight plugin wrapper around the constructor, 
    // preventing against multiple instantiations
    $.fn[pluginName] = function ( options ) 
    {
        return this.each(function () {
            if (!$.data(this, 'plugin_' + pluginName)) 
            {
                $.data(this, 'plugin_' + pluginName, 
                new Plugin( this, options ));
            }
        });
    };

})( jQuery, window, document ); // jshint ignore: line
