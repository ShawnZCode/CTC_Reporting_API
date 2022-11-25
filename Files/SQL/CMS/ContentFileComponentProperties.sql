/****** Object:  Table [dbo].[ContentFileComponentProperties]    Script Date: 11/17/2022 4:20:39 PM ******/
SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [dbo].[ContentFileComponentProperties](
	[id] [uniqueidentifier] NOT NULL,
	[contentFileComponentId] [uniqueidentifier] NOT NULL,
	[isInstance] [bit] NULL,
	[isReadOnly] [bit] NULL,
	[name] [nvarchar](100) NOT NULL,
	[revitParameterGroupId] [int] NULL,
	[revitParameterTypeId] [int] NULL,
	[revitSharedParameterGuid] [uniqueidentifier] NULL,
	[revitStorageTypeId] [int] NULL,
	[revitDisplayUnitTypeId] [int] NULL,
	[doubleValue] [float] NULL,
	[type] [int] NOT NULL,
	[value] [nvarchar](2048) NULL,
	[unitTypeIdVersionless] [nvarchar](100) NULL,
	CONSTRAINT [PK_ContentFileComponentProperties] PRIMARY KEY CLUSTERED 
		([id] ASC)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
	) ON [PRIMARY]

ALTER TABLE [dbo].[ContentFileComponentProperties] ADD  DEFAULT ((0)) FOR [type]
