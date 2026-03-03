---
name: 38 Remotion Video Editor
description: Programmatic video generation using React. Creating marketing videos or animations via code.
version: 1.0.0
---

# 38 Remotion Video Editor

Execute programmatic video creation and animation workflows using Remotion.

## 1. Composition Rules
- **Component Splits:** Break videos down into smaller, reusable React components (`<Sequence>`, `<Series>`).
- **FPS & Dimensions:** Always explicitly define `fps` (30 or 60), `width` (1920 or 1080 for shorts), and `height`.

## 2. Animation Principles
- **Spring Physics:** Use Remotion's `spring()` for natural-feeling motions over linear easings.
- **Interpolation:** Master `interpolate()` for mapping frame numbers to opacities, scales, and translations.

## 3. Asset Management
- **Pre-loading:** Ensure all dynamic assets (images, external fonts, audio) are pre-loaded or explicitly awaited in Remotion to avoid blank frames during rendering.
- **Audio Sync:** Carefully synchronize audio waveforms and audio components with the `useCurrentFrame()` logic.
