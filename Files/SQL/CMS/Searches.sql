/****** Object:  Table [dbo].[Searches]    Script Date: 11/17/2022 4:26:41 PM ******/
SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [dbo].[Searches](
	[id] [uniqueidentifier] NOT NULL,
	[organizationId] [uniqueidentifier] NOT NULL,
	[savedSearchId] [uniqueidentifier] NULL,
	[query] [nvarchar](100) NULL,
	[sortBy] [nvarchar](10) NOT NULL,
	[sortDirection] [nvarchar](10) NOT NULL,
	[minAvgRating] [int] NULL,
	[addedStartDate] [datetime2](7) NULL,
	[addedEndDate] [datetime2](7) NULL,
	[addedByUser] [nvarchar](max) NULL,
	[updateStartDate] [datetime2](7) NULL,
	[updatedEndDate] [datetime2](7) NULL,
	[updatedByUser] [nvarchar](max) NULL,
	[searchedAt] [datetime2](7) NOT NULL,
	[searchedById] [uniqueidentifier] NOT NULL,
	[executionTimeInMs] [bigint] NOT NULL,
	[page] [int] NOT NULL,
	[pageSize] [int] NOT NULL,
	[searchId] [uniqueidentifier] NOT NULL,
	[resultCount] [int] NOT NULL,
	[savedSearchName] [nvarchar](100) NULL,
	[hasExplicitLibraryFilter] [bit] NOT NULL,
	[displayUnits] [nvarchar](100) NULL,
	[fileVersions] [nvarchar](100) NULL,
	CONSTRAINT [PK_Searches] PRIMARY KEY CLUSTERED 
	(
		[id] ASC
	)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
	) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]

ALTER TABLE [dbo].[Searches] ADD  DEFAULT (CONVERT([bigint],(0))) FOR [executionTimeInMs]

ALTER TABLE [dbo].[Searches] ADD  DEFAULT ((0)) FOR [page]

ALTER TABLE [dbo].[Searches] ADD  DEFAULT ((0)) FOR [pageSize]

ALTER TABLE [dbo].[Searches] ADD  DEFAULT ('00000000-0000-0000-0000-000000000000') FOR [searchId]

ALTER TABLE [dbo].[Searches] ADD  DEFAULT ((0)) FOR [resultCount]

ALTER TABLE [dbo].[Searches] ADD  DEFAULT (CONVERT([bit],(0))) FOR [hasExplicitLibraryFilter]
