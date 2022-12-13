/****** Object:  Table [CMS].[Feedbacks]    Script Date: 11/17/2022 4:22:17 PM ******/
SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [CMS].[Feedbacks](
	[id] [uniqueidentifier] NOT NULL,
	[organizationId] [uniqueidentifier] NOT NULL,
	[description] [nvarchar](2048) NULL,
	[type] [int] NOT NULL,
	[screenshotCount] [int] NOT NULL,
	[attachmentCount] [int] NOT NULL,
	[submittedAt] [datetimeoffset](7) NOT NULL,
	[submittedById] [uniqueidentifier] NOT NULL,
	[logFileCount] [int] NOT NULL,
	[refreshedId] [uniqueidentifier] NOT NULL,
	CONSTRAINT [PK_Feedbacks] PRIMARY KEY CLUSTERED 
		([id] ASC)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
	) ON [PRIMARY]

ALTER TABLE [CMS].[Feedbacks] ADD  DEFAULT ((0)) FOR [logFileCount]
