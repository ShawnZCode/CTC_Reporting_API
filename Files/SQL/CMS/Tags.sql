/****** Object:  Table [dbo].[Tags]    Script Date: 11/17/2022 4:28:18 PM ******/
SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [dbo].[Tags](
	[id] [uniqueidentifier] NOT NULL,
	[addedAt] [datetime2](7) NOT NULL,
	[addedById] [uniqueidentifier] NOT NULL,
	[updatedAt] [datetime2](7) NOT NULL,
	[updatedById] [uniqueidentifier] NOT NULL,
	[name] [nvarchar](100) NOT NULL,
	[organizationId] [uniqueidentifier] NOT NULL,
	[description] [nvarchar](2048) NULL,
	[updatedId] [uniqueidentifier] NOT NULL,
	CONSTRAINT [PK_Tags] PRIMARY KEY CLUSTERED 
	(
		[id] ASC
	)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
	) ON [PRIMARY]
