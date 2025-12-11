# Spotify Streaming Analysis

An exploratory data analysis of music streaming metrics across multiple platforms to identify key drivers of track success.

## Overview

This project analyzes streaming data from Spotify, YouTube, TikTok, Apple Music, and other platforms to understand what factors correlate with streaming success. Using correlation analysis and visualization techniques, the analysis identifies playlist placement as the strongest predictor of streaming performance.

## Key Findings

- **Playlist placement is the dominant success factor** - Spotify playlist count shows the strongest correlation with streams (r=0.85), indicating that editorial and algorithmic playlist inclusion is critical for track success

- **Cross-platform presence matters** - YouTube views correlate moderately with Spotify streams (r=0.57), suggesting that multi-platform presence contributes to overall track performance, though platforms measure success differently

- **Apple Music vs Spotify metrics** - Apple Music playlist counts (hundreds) represent curated editorial placements, while Spotify counts (tens of thousands) include user-generated playlists, yet both correlate strongly with their respective streaming numbers

- **US market focus** - The dataset is primarily US-centric (~78% US-registered ISRC codes), limiting the generalizability of findings to global music markets

## Dataset

The analysis uses a music streaming dataset containing:
- Streaming metrics (Spotify, YouTube, TikTok, Pandora, SoundCloud, etc.)
- Playlist placements across platforms
- Track metadata (ISRC codes, explicit content flags)
- Engagement metrics (likes, views, posts)

**Note:** Dataset origin and validation status unknown - this is an exploratory exercise.

## Technical Approach

### Data Cleaning
- Converted numeric columns with comma formatting to proper numeric types
- Handled missing values with appropriate strategies (fillna, filtering)
- Extracted country codes from ISRC identifiers
- Applied log scaling to handle wide range of streaming values

### Analysis Methods
- **Correlation analysis** using Spearman correlation (appropriate for skewed streaming data)
- **Distribution analysis** using KDE plots to understand data shape
- **Comparative analysis** across platforms and track characteristics
- **Visualization** with seaborn and matplotlib for pattern identification

### Key Technical Decisions
- **Spearman over Pearson** - Streaming data is heavily right-skewed with outliers; Spearman's rank-based approach handles this better
- **Log scaling** - Applied to visualizations to reveal patterns across orders of magnitude
- **Zero filtering** - Excluded zero values when calculating correlations to avoid distortion from tracks not present on certain platforms

## Tools & Technologies

- **Python 3.x** - Primary language
- **pandas** - Data manipulation and analysis
- **seaborn & matplotlib** - Visualization
- **scipy.stats** - Statistical correlation analysis
- **numpy** - Numerical operations

## Key Insights for Music Industry

1. **For independent artists**: Focus efforts on playlist pitching and securing placements rather than solely on production quality or marketing spend

2. **Platform strategy**: Multi-platform presence shows moderate correlation, suggesting diversified distribution has value, though Spotify playlist placement remains the primary driver

3. **Measurement differences**: Platform metrics aren't directly comparable (Apple's editorial focus vs Spotify's user-generated scale), requiring context-specific interpretation

## Limitations

- Dataset provenance unclear - unable to verify data quality or collection methodology
- US market bias limits global applicability
- No temporal data - unable to analyze trends over time or causality (do playlists drive streams, or do streams drive playlist adds?)
- Correlation ≠ causation - playlist placement and streams likely have bidirectional relationship with confounding variables

## Project Purpose

This is a **practice project** focused on:
- Exploratory data analysis techniques
- Working with real-world messy data
- Statistical correlation analysis
- Data visualization best practices
- Applying domain knowledge (music industry) to data interpretation

## Repository Structure

```
├── analysis.ipynb          # Main analysis notebook
├── data/                   # Dataset (if shareable)
├── visualizations/         # Generated plots and charts
└── README.md              # This file
```

## Future Improvements

If expanding this analysis:
- Time-series analysis to understand catalog vs new release dynamics
- Genre-specific patterns and success factors
- Predictive modeling for stream forecasting
- Causality analysis using temporal data
- Geographic/market-specific segmentation
- 
---

*Analysis completed as part of data analysis portfolio development*
