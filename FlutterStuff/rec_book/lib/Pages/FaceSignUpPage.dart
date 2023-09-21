import 'dart:typed_data';
import 'package:flutter/material.dart';
import 'package:camera/camera.dart';
import 'package:google_ml_kit/google_ml_kit.dart';

class FaceSignUpPage extends StatefulWidget {
  @override
  _FaceSignUpPageState createState() => _FaceSignUpPageState();
}

class _FaceSignUpPageState extends State<FaceSignUpPage> {
  late CameraController _controller;
  late FaceDetector _faceDetector;
  List<Rect> _detectedFaces = [];

  @override
  void initState() {
    super.initState();

    _controller = CameraController(
      CameraDescription(
        name: 'Camera',
        lensDirection: CameraLensDirection.front,
      ),
      ResolutionPreset.medium,
    );

    _faceDetector = GoogleMlKit.vision.faceDetector(
      FaceDetectorOptions(
        enableClassification: false,
        enableTracking: false,
        enableContours: true,
      ),
    );

    _controller.initialize().then((_) {
      if (!mounted) {
        return;
      }
      setState(() {});
      _controller.startImageStream((CameraImage img) {
        _detectFaces(img);
      });
    });
  }

  void _detectFaces(CameraImage image) async { 
    final inputImage = InputImage.fromBytes( 
      bytes: _concatenatePlanes(image.planes),
      inputImageData: InputImageData(
        inputImageFormat: InputImageFormatMethods.fromRawValue(image.format.raw) ?? InputImageFormat.NV21,
        size: Size(image.width.toDouble(), image.height.toDouble()),
        rotation: InputImageRotation.Rotation_90deg, 
        planeData: image.planes.map((plane) {
          return InputImagePlaneMetadata(
            bytesPerRow: plane.bytesPerRow,
            height: plane.height,
            width: plane.width,
          );
        }).toList(),
      ),
    );

    final faces = await _faceDetector.processImage(inputImage);
    for (Face face in faces) {
      print('face BoundingBox Yo: ${face.boundingBox}');
    }

    setState(() {
      _detectedFaces = faces.map((face) => face.boundingBox).toList();
    });
  }

  Uint8List _concatenatePlanes(List<Plane> planes) {
    final WriteBuffer allBytes = WriteBuffer();
    for (Plane plane in planes) {
      allBytes.putUint8List(plane.bytes);
    }
    return allBytes.done().buffer.asUint8List();
  }

  @override
  Widget build(BuildContext context) {
    if (!_controller.value.isInitialized) {
      return Container();
    }
    return Scaffold(
      appBar: AppBar(
        title: Text('Signing Up Face'),
      ),
      body: Center(
        child: AspectRatio(
          aspectRatio: _controller.value.aspectRatio,
          child: Stack(
            children: [
              CameraPreview(_controller),
              CustomPaint(
                painter: BoundingBoxPainter(_detectedFaces),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class BoundingBoxPainter extends CustomPainter {
  final List<Rect> faces;

  BoundingBoxPainter(this.faces);

  @override
  void paint(Canvas canvas, Size size) {
    final paint = Paint()
      ..color = Colors.red
      ..style = PaintingStyle.stroke 
      ..strokeWidth = 2.0;

    for (final rect in faces) {
      canvas.drawRect(rect, paint);
    }
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) {
    return true;
  }
}
