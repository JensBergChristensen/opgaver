import './style.css';
import {Map, View} from 'ol';
import TileLayer from 'ol/layer/Tile';
import OSM from 'ol/source/OSM';
import {fromLonLat} from 'ol/proj';
import Feature from 'ol/Feature';
import {transform} from 'ol/proj';
import Style from 'ol/style/Style';
import VectorLayer from 'ol/layer/Vector';
import VectorSource from 'ol/source/Vector';
import Point from 'ol/geom/Point';
import Icon from 'ol/style/Icon';

const map = new Map({
  target: 'map',
  layers: [
    new TileLayer({
      source: new OSM()
    }),
  ],
  view: new View({
    center: fromLonLat([9.92, 57.03]),
    zoom: 14
  })
});

function add_map_point(lng, lat) {
  var vectorLayer = new VectorLayer({
    source:new VectorSource({
      features: [new Feature({
            geometry: new Point(transform([parseFloat(lng), parseFloat(lat)], 'EPSG:4326', 'EPSG:3857')),
        })]
    }),
    style: new Style({
      image: new Icon({
        anchor: [0.5, 0.5],
        anchorXUnits: "fraction",
        anchorYUnits: "fraction",
        src: "https://upload.wikimedia.org/wikipedia/commons/e/ec/RedDot.svg"
      })
    })
  });

  map.addLayer(vectorLayer);
}



add_map_point(9.885379713136524, 57.02086591844645)


map.on('dblclick', function (evt) {
  console.log(transform(evt.coordinate, 'EPSG:3857', 'EPSG:4326'));
});
