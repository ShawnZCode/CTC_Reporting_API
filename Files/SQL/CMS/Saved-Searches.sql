/****** Object:  Table [dbo].[SavedSearches]    Script Date: 11/17/2022 4:23:50 PM ******/
SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [dbo].[Saved-Searches](
	[id] [uniqueidentifier] NOT NULL,
	[addedAt] [datetime2](7) NOT NULL,
	[addedById] [uniqueidentifier] NOT NULL,
	[updatedAt] [datetime2](7) NOT NULL,
	[updatedById] [uniqueidentifier] NOT NULL,
	[name] [nvarchar](100) NOT NULL,
	[organizationId] [uniqueidentifier] NOT NULL,
	[scope] [nvarchar](20) NOT NULL,
	[description] [nvarchar](2048) NULL,
	[query] [nvarchar](100) NULL,
	[sortBy] [nvarchar](10) NOT NULL,
	[sortDirection] [nvarchar](10) NOT NULL,
	[minAvgRating] [int] NULL,
	[addedStartDate] [datetime2](7) NULL,
	[addedEndDate] [datetime2](7) NULL,
	[updateStartDate] [datetime2](7) NULL,
	[updatedEndDate] [datetime2](7) NULL,
	[addedByUser] [nvarchar](max) NULL,
	[updatedByUser] [nvarchar](max) NULL,
	[displayUnits] [nvarchar](100) NULL,
	[fileVersions] [nvarchar](100) NULL,
	[filterContentByNotTagged] [bit] NOT NULL,
	[fileExtensions] [nvarchar](100) NULL,
	[revitFamilyHostTypes] [nvarchar](13) NULL,
	CONSTRAINT [PK_Saved-Searches] PRIMARY KEY CLUSTERED 
	(
		[id] ASC
	)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
	) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]

ALTER TABLE [dbo].[Saved-Searches] ADD  DEFAULT (CONVERT([bit],(0))) FOR [filterContentByNotTagged]
