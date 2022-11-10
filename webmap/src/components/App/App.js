import React from "react";
import Map from "../Map/Map";
import {AlertDismissible} from '../Notes/Notes';

function App() {
  return (
      <React.Fragment>
        <AlertDismissible/>
        <div>
          <h2 className={"d-flex justify-content-center pt-3 pb-3"}>
            IMOS SST & Rio-tiler 🛰️🗺️
          </h2>
        </div>
        <Map/>
      </React.Fragment>
  )
}

export default App;
