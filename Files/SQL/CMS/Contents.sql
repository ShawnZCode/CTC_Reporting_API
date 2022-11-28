/****** Object:  Table [dbo].[Contents]    Script Date: 11/17/2022 4:18:17 PM ******/
SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON

CREATE TABLE [dbo].[Contents](
	[id] [uniqueidentifier] NOT NULL,
	[addedAt] [datetime2](7) NOT NULL,
	[addedById] [uniqueidentifier] NOT NULL,
	[updatedAt] [datetime2](7) NOT NULL,
	[updatedById] [uniqueidentifier] NOT NULL,
	[name] [nvarchar](150) NOT NULL,
	[fileName] [nvarchar](150) NOT NULL,
	[fileExtension] [nvarchar](13) NOT NULL,
	[organizationId] [uniqueidentifier] NOT NULL,
	[hasCustomPreviewImage] [bit] NOT NULL,
	[type] [nvarchar](30) NOT NULL,
	[source] [nvarchar](30) NOT NULL,
	[location] [nvarchar](20) NOT NULL,
	[averageRating] [float] NOT NULL,
	[revitCategoryId] [int] NULL,
	[previewImageUri] [nvarchar](2048) NULL,
	[displayUnit] [nvarchar](10) NULL,
	[revitFamilyHostType] [nvarchar](20) NULL,
	[updatedId] [uniqueidentifier] NOT NULL,
	CONSTRAINT [PK_Contents] PRIMARY KEY CLUSTERED 
		([id] ASC)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
	) ON [PRIMARY]
