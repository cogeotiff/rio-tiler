import React, { useState } from 'react';
import Alert from 'react-bootstrap/Alert';
import Button from 'react-bootstrap/Button';

export function AlertDismissible() {
  const [show, setShow] = useState(true);
  return (
    <>
      <Alert show={show} variant="success">
        <Alert.Heading>Notes:</Alert.Heading>
        <div>
          <ul>
            <li>
              Just a simple POC to justify whether IMOS SST can be visualised on a webmap like Leaflet using Rio-tiler XarrayReader feature.
            </li>
            <li>
              Consider tile caching strategies if this ever go to production.
            </li>
          </ul>
        </div>
        <hr />
        <div className="d-flex justify-content-end">
          <Button onClick={() => setShow(false)} variant="outline-success">
            Close
          </Button>
        </div>
      </Alert>
      {!show && <Button className={"mt-3 m-lg-3"} onClick={() => setShow(true)}>Show Notes</Button>}
    </>
  );
}
