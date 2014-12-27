var LayerSlider = function () {

    return {

        //Layer Slider
        initLayerSlider: function () {
		    $(document).ready(function(){
		        jQuery("#layerslider").layerSlider({
			        skin: 'fullwidth',
			        responsive : true,
			        responsiveUnder : 960,
			        layersContainer : 960,
                    showCircleTimer : false,
			        skinsPath: '/static/assets/plugins/layer-slider/layerslider/skins/'
			    });
		    });
        }

    };
}();