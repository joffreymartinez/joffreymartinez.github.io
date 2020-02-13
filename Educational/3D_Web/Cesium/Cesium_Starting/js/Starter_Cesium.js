// Grant CesiumJS access to your ion assets
Cesium.Ion.defaultAccessToken = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI2YjI1ZDlkNi01YTAwLTRjZGUtYmMxMi1mZDM0ZWQ2ZTUxYjAiLCJpZCI6MjE2OTQsInNjb3BlcyI6WyJhc3IiLCJnYyJdLCJpYXQiOjE1ODAzMjU5ODl9.Q9uhPf1xCh8R4tBsIGlWwbBdhalj9Vzr-GNjdr2OYTI';

var viewer = new Cesium.Viewer('cesiumContainer', {
  terrainProvider: Cesium.createWorldTerrain()
});
// var tileset = viewer.scene.primitives.add(
//   new Cesium.Cesium3DTileset({
//     url:Cesium.IonResource.fromAssetId(72933)
//   })
// );
var layer1 = viewer.imageryLayers.addImageryProvider(
  new Cesium.IonImageryProvider({ assetId:3812})
);
var promise = Cesium.IonResource.fromAssetId(73368)
.then(function (resource) {
    return Cesium.KmlDataSource.load(resource, {
        camera: viewer.scene.camera,
        canvas: viewer.scene.canvas
    });
});

var canada1 = Cesium.Ionresource.fromAssetID(73368)
  .then (function (resource) {
    return Cesium.KmlDataSource.load(resource,{
    camera: viewer.scene.camera,
    canvas: viewer.scene.canvas
  });
});