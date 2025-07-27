from ultralytics import YOLO

model = YOLO('models/best.pt')
results = model.predict('input_videos/08fd33_4.mp4', save=True)
print(results[0])
print("========================================================================================")
for box in results[0].boxes:
  print(box)

# STREAM VERSION OF THIS CODE

# def stream_inference():
#   model = YOLO('models/best.pt')
  
#   # Use stream=True to process frames one by one without accumulating in RAM
#   results = model.predict('input_videos/08fd33_4.mp4', save=True, stream=True)
  
#   print("Processing video with streaming inference...")
#   frame_count = 0
  
#   for result in results:
#       frame_count += 1
#       print(f"Frame {frame_count}:")
#       print(f"  Detected objects: {len(result.boxes)} boxes")
      
#       # Print details of first few frames only to avoid spam
#       if frame_count <= 3:
#           print(f"  Result summary: {result}")
#           print("  Box details:")
#           for i, box in enumerate(result.boxes):
#               if i < 5:  # Print first 5 boxes only
#                   print(f"    Box {i+1}: {box}")
#           print("=" * 50)
      
#       # Optional: Break early for testing
#       # if frame_count >= 10:
#       #     break
  
#   print(f"Total frames processed: {frame_count}")
#   print(f"Detected object names: {model.names}")

# stream_inference()

