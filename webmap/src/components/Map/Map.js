import React, { Component } from 'react';
import './Map.css'
import { MapContainer, TileLayer, LayerGroup} from 'react-leaflet'

class Map extends Component {
  render(){
    const position = [-30, 135];
    return (
      <React.Fragment>
        <MapContainer center={position} zoom={4} scrollWheelZoom={false}>
          {/*<TileLayer*/}
          {/*  url="http://127.0.0.1:8000/tiles/{z}/{x}/{y}?url=s3%3A%2F%2Fimos-data-pixeldrill%2Fvhnguyen%2Fplayground%2Fmulti-years&variable=sea_surface_temperature&idx=7000"*/}
          {/*/>*/}
          <TileLayer
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          />
          <LayerGroup>
            <TileLayer
              url="http://127.0.0.1:8000/tiles/{z}/{x}/{y}?url=s3%3A%2F%2Fimos-data-pixeldrill%2Fvhnguyen%2Fplayground%2Fmulti-years&variable=sea_surface_temperature&idx=7000"
            />
          </LayerGroup>
        </MapContainer>
    </React.Fragment>);
  }
}


export default Map;