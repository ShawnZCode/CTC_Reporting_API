
/*** Alter Contents ***/
ALTER TABLE [dbo].[Contents]  WITH CHECK ADD  CONSTRAINT [FK_Contents_Users_addedById] FOREIGN KEY([addedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[Contents] CHECK CONSTRAINT [FK_Contents_Users_addedById]

ALTER TABLE [dbo].[Contents]  WITH CHECK ADD  CONSTRAINT [FK_Contents_Users_updatedById] FOREIGN KEY([updatedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[Contents] CHECK CONSTRAINT [FK_Contents_Users_updatedById]

/*** Alter ContentAtachments ***/
ALTER TABLE [dbo].[ContentAttachments]  WITH CHECK ADD  CONSTRAINT [FK_ContentAttachments_Contents_contentId] FOREIGN KEY([contentId])
REFERENCES [dbo].[Contents] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[ContentAttachments] CHECK CONSTRAINT [FK_ContentAttachments_Contents_contentId]

ALTER TABLE [dbo].[ContentAttachments]  WITH CHECK ADD  CONSTRAINT [FK_ContentAttachments_Users_addedById] FOREIGN KEY([addedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[ContentAttachments] CHECK CONSTRAINT [FK_ContentAttachments_Users_addedById]

ALTER TABLE [dbo].[ContentAttachments]  WITH CHECK ADD  CONSTRAINT [FK_ContentAttachments_Users_updatedById] FOREIGN KEY([updatedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[ContentAttachments] CHECK CONSTRAINT [FK_ContentAttachments_Users_updatedById]

/*** Alter ContentDownloads ***/
ALTER TABLE [dbo].[ContentDownloads]  WITH CHECK ADD  CONSTRAINT [FK_ContentDownloads_Contents_contentId] FOREIGN KEY([contentId])
REFERENCES [dbo].[Contents] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[ContentDownloads] CHECK CONSTRAINT [FK_ContentDownloads_Contents_contentId]

ALTER TABLE [dbo].[ContentDownloads]  WITH CHECK ADD  CONSTRAINT [FK_ContentDownloads_Users_downloadedById] FOREIGN KEY([downloadedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[ContentDownloads] CHECK CONSTRAINT [FK_ContentDownloads_Users_downloadedById]

/*** Alter ContentFileComponentProperties ***/
ALTER TABLE [dbo].[ContentFileComponentProperties]  WITH CHECK ADD  CONSTRAINT [FK_ContentFileComponentProperties_ContentFileComponents_contentFileComponentId] FOREIGN KEY([contentFileComponentId])
REFERENCES [dbo].[ContentFileComponents] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[ContentFileComponentProperties] CHECK CONSTRAINT [FK_ContentFileComponentProperties_ContentFileComponents_contentFileComponentId]

/*** Alter ContentFileComponents ***/
ALTER TABLE [dbo].[ContentFileComponents]  WITH CHECK ADD  CONSTRAINT [FK_ContentFileComponents_ContentFiles_contentFileId] FOREIGN KEY([contentFileId])
REFERENCES [dbo].[ContentFiles] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[ContentFileComponents] CHECK CONSTRAINT [FK_ContentFileComponents_ContentFiles_contentFileId]

/*** Alter ContentFiles ***/

ALTER TABLE [dbo].[ContentFiles]  WITH CHECK ADD  CONSTRAINT [FK_ContentFiles_Contents_contentId] FOREIGN KEY([contentId])
REFERENCES [dbo].[Contents] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[ContentFiles] CHECK CONSTRAINT [FK_ContentFiles_Contents_contentId]

ALTER TABLE [dbo].[ContentFiles]  WITH CHECK ADD  CONSTRAINT [FK_ContentFiles_Users_addedById] FOREIGN KEY([addedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[ContentFiles] CHECK CONSTRAINT [FK_ContentFiles_Users_addedById]

ALTER TABLE [dbo].[ContentFiles]  WITH CHECK ADD  CONSTRAINT [FK_ContentFiles_Users_updatedById] FOREIGN KEY([updatedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[ContentFiles] CHECK CONSTRAINT [FK_ContentFiles_Users_updatedById]

/*** Alter ContentLibraries ***/
ALTER TABLE [dbo].[ContentLibraries]  WITH CHECK ADD  CONSTRAINT [FK_ContentLibraries_Contents_contentId] FOREIGN KEY([contentId])
REFERENCES [dbo].[Contents] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[ContentLibraries] CHECK CONSTRAINT [FK_ContentLibraries_Contents_contentId]

ALTER TABLE [dbo].[ContentLibraries]  WITH CHECK ADD  CONSTRAINT [FK_ContentLibraries_Libraries_libraryId] FOREIGN KEY([libraryId])
REFERENCES [dbo].[Libraries] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[ContentLibraries] CHECK CONSTRAINT [FK_ContentLibraries_Libraries_libraryId]

/*** Alter ContentLoads ***/

ALTER TABLE [dbo].[ContentLoads]  WITH CHECK ADD  CONSTRAINT [FK_ContentLoads_Contents_contentId] FOREIGN KEY([contentId])
REFERENCES [dbo].[Contents] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[ContentLoads] CHECK CONSTRAINT [FK_ContentLoads_Contents_contentId]

ALTER TABLE [dbo].[ContentLoads]  WITH CHECK ADD  CONSTRAINT [FK_ContentLoads_Documents_documentId] FOREIGN KEY([documentId])
REFERENCES [dbo].[Documents] ([id])

ALTER TABLE [dbo].[ContentLoads] CHECK CONSTRAINT [FK_ContentLoads_Documents_documentId]

ALTER TABLE [dbo].[ContentLoads]  WITH CHECK ADD  CONSTRAINT [FK_ContentLoads_Searches_searchId] FOREIGN KEY([searchId])
REFERENCES [dbo].[Searches] ([id])

ALTER TABLE [dbo].[ContentLoads] CHECK CONSTRAINT [FK_ContentLoads_Searches_searchId]

ALTER TABLE [dbo].[ContentLoads]  WITH CHECK ADD  CONSTRAINT [FK_ContentLoads_Users_loadedById] FOREIGN KEY([loadedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[ContentLoads] CHECK CONSTRAINT [FK_ContentLoads_Users_loadedById]

/*** Alter ContentReviews ***/
ALTER TABLE [dbo].[ContentReviews]  WITH CHECK ADD  CONSTRAINT [FK_ContentReviews_Contents_contentId] FOREIGN KEY([contentId])
REFERENCES [dbo].[Contents] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[ContentReviews] CHECK CONSTRAINT [FK_ContentReviews_Contents_contentId]

ALTER TABLE [dbo].[ContentReviews]  WITH CHECK ADD  CONSTRAINT [FK_ContentReviews_Users_addedById] FOREIGN KEY([addedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[ContentReviews] CHECK CONSTRAINT [FK_ContentReviews_Users_addedById]

ALTER TABLE [dbo].[ContentReviews]  WITH CHECK ADD  CONSTRAINT [FK_ContentReviews_Users_updatedById] FOREIGN KEY([updatedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[ContentReviews] CHECK CONSTRAINT [FK_ContentReviews_Users_updatedById]

/*** Content Revisions ***/
ALTER TABLE [dbo].[ContentRevisions]  WITH CHECK ADD  CONSTRAINT [FK_ContentRevisions_Contents_contentId] FOREIGN KEY([contentId])
REFERENCES [dbo].[Contents] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[ContentRevisions] CHECK CONSTRAINT [FK_ContentRevisions_Contents_contentId]

ALTER TABLE [dbo].[ContentRevisions]  WITH CHECK ADD  CONSTRAINT [FK_ContentRevisions_Users_revisedById] FOREIGN KEY([revisedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[ContentRevisions] CHECK CONSTRAINT [FK_ContentRevisions_Users_revisedById]

/*** Alter ContentTags ***/
ALTER TABLE [dbo].[ContentTags]  WITH CHECK ADD  CONSTRAINT [FK_ContentTags_Contents_contentId] FOREIGN KEY([contentId])
REFERENCES [dbo].[Contents] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[ContentTags] CHECK CONSTRAINT [FK_ContentTags_Contents_contentId]

ALTER TABLE [dbo].[ContentTags]  WITH CHECK ADD  CONSTRAINT [FK_ContentTags_Tags_tagId] FOREIGN KEY([tagId])
REFERENCES [dbo].[Tags] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[ContentTags] CHECK CONSTRAINT [FK_ContentTags_Tags_tagId]

/*** Alter Documents (NotNeeded) ***/

/*** Alter Feedbacks ***/
ALTER TABLE [dbo].[Feedbacks]  WITH CHECK ADD  CONSTRAINT [FK_Feedbacks_Users_submittedById] FOREIGN KEY([submittedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[Feedbacks] CHECK CONSTRAINT [FK_Feedbacks_Users_submittedById]

/*** Alter Libraries ***/
ALTER TABLE [dbo].[Libraries]  WITH CHECK ADD  CONSTRAINT [FK_Libraries_Users_addedById] FOREIGN KEY([addedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[Libraries] CHECK CONSTRAINT [FK_Libraries_Users_addedById]

ALTER TABLE [dbo].[Libraries]  WITH CHECK ADD  CONSTRAINT [FK_Libraries_Users_updatedById] FOREIGN KEY([updatedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[Libraries] CHECK CONSTRAINT [FK_Libraries_Users_updatedById]

/*** Alter LibraryPermissions ***/
ALTER TABLE [dbo].[LibraryPermissions]  WITH CHECK ADD  CONSTRAINT [FK_LibraryPermissions_Libraries_libraryId] FOREIGN KEY([libraryId])
REFERENCES [dbo].[Libraries] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[LibraryPermissions] CHECK CONSTRAINT [FK_LibraryPermissions_Libraries_libraryId]

ALTER TABLE [dbo].[LibraryPermissions]  WITH CHECK ADD  CONSTRAINT [FK_LibraryPermissions_LibrarySubscriptions_librarySubscriptionId] FOREIGN KEY([librarySubscriptionId])
REFERENCES [dbo].[LibrarySubscriptions] ([id])

ALTER TABLE [dbo].[LibraryPermissions] CHECK CONSTRAINT [FK_LibraryPermissions_LibrarySubscriptions_librarySubscriptionId]

ALTER TABLE [dbo].[LibraryPermissions]  WITH CHECK ADD  CONSTRAINT [FK_LibraryPermissions_Users_addedById] FOREIGN KEY([addedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[LibraryPermissions] CHECK CONSTRAINT [FK_LibraryPermissions_Users_addedById]

ALTER TABLE [dbo].[LibraryPermissions]  WITH CHECK ADD  CONSTRAINT [FK_LibraryPermissions_Users_updatedById] FOREIGN KEY([updatedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[LibraryPermissions] CHECK CONSTRAINT [FK_LibraryPermissions_Users_updatedById]

/*** Alter SavedSearchContentSources ***/
ALTER TABLE [dbo].[SavedSearchContentSources]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearchContentSources_SavedSearches_savedSearchId] FOREIGN KEY([savedSearchId])
REFERENCES [dbo].[SavedSearches] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[SavedSearchContentSources] CHECK CONSTRAINT [FK_SavedSearchContentSources_SavedSearches_savedSearchId]

/*** Alter SavedSearches ***/

ALTER TABLE [dbo].[SavedSearches]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearches_Users_addedById] FOREIGN KEY([addedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[SavedSearches] CHECK CONSTRAINT [FK_SavedSearches_Users_addedById]

ALTER TABLE [dbo].[SavedSearches]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearches_Users_updatedById] FOREIGN KEY([updatedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[SavedSearches] CHECK CONSTRAINT [FK_SavedSearches_Users_updatedById]

/*** Alter SavedSearchLibraries ***/
ALTER TABLE [dbo].[SavedSearchLibraries]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearchLibraries_Libraries_libraryId] FOREIGN KEY([libraryId])
REFERENCES [dbo].[Libraries] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[SavedSearchLibraries] CHECK CONSTRAINT [FK_SavedSearchLibraries_Libraries_libraryId]

ALTER TABLE [dbo].[SavedSearchLibraries]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearchLibraries_SavedSearches_savedSearchId] FOREIGN KEY([savedSearchId])
REFERENCES [dbo].[SavedSearches] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[SavedSearchLibraries] CHECK CONSTRAINT [FK_SavedSearchLibraries_SavedSearches_savedSearchId]

/*** Alter SavedSearchPermissions ***/
ALTER TABLE [dbo].[SavedSearchPermissions]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearchPermissions_SavedSearches_savedSearchId] FOREIGN KEY([savedSearchId])
REFERENCES [dbo].[SavedSearches] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[SavedSearchPermissions] CHECK CONSTRAINT [FK_SavedSearchPermissions_SavedSearches_savedSearchId]

ALTER TABLE [dbo].[SavedSearchPermissions]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearchPermissions_Users_addedById] FOREIGN KEY([sddedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[SavedSearchPermissions] CHECK CONSTRAINT [FK_SavedSearchPermissions_Users_addedById]

ALTER TABLE [dbo].[SavedSearchPermissions]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearchPermissions_Users_updatedById] FOREIGN KEY([updatedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[SavedSearchPermissions] CHECK CONSTRAINT [FK_SavedSearchPermissions_Users_updatedById]

/*** Alter SavedSearchCategories ***/
ALTER TABLE [dbo].[SavedSearchRevitCategories]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearchRevitCategories_SavedSearches_savedSearchId] FOREIGN KEY([savedSearchId])
REFERENCES [dbo].[SavedSearches] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[SavedSearchRevitCategories] CHECK CONSTRAINT [FK_SavedSearchRevitCategories_SavedSearches_savedSearchId]

/*** Alter SavedSearchTags ***/
ALTER TABLE [dbo].[SavedSearchTags]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearchTags_SavedSearches_savedSearchId] FOREIGN KEY([savedSearchId])
REFERENCES [dbo].[SavedSearches] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[SavedSearchTags] CHECK CONSTRAINT [FK_SavedSearchTags_SavedSearches_savedSearchId]

ALTER TABLE [dbo].[SavedSearchTags]  WITH CHECK ADD  CONSTRAINT [FK_SavedSearchTags_Tags_tagId] FOREIGN KEY([tagId])
REFERENCES [dbo].[Tags] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[SavedSearchTags] CHECK CONSTRAINT [FK_SavedSearchTags_Tags_tagId]

/*** Alter SearchContentSources ***/
ALTER TABLE [dbo].[SearchContentSources]  WITH CHECK ADD  CONSTRAINT [FK_SearchContentSources_Searches_searchId] FOREIGN KEY([searchId])
REFERENCES [dbo].[Searches] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[SearchContentSources] CHECK CONSTRAINT [FK_SearchContentSources_Searches_searchId]

/*** Alter Searches ***/
ALTER TABLE [dbo].[Searches]  WITH CHECK ADD  CONSTRAINT [FK_Searches_Users_searchedById] FOREIGN KEY([searchedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[Searches] CHECK CONSTRAINT [FK_Searches_Users_searchedById]

/*** Alter SearchLibraries ***/
ALTER TABLE [dbo].[SearchLibraries]  WITH CHECK ADD  CONSTRAINT [FK_SearchLibraries_Searches_searchId] FOREIGN KEY([searchId])
REFERENCES [dbo].[Searches] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[SearchLibraries] CHECK CONSTRAINT [FK_SearchLibraries_Searches_searchId]

/*** Alter SearchResults ***/
ALTER TABLE [dbo].[SearchResults]  WITH CHECK ADD  CONSTRAINT [FK_SearchResults_Searches_searchId] FOREIGN KEY([searchId])
REFERENCES [dbo].[Searches] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[SearchResults] CHECK CONSTRAINT [FK_SearchResults_Searches_searchId]

/*** Alter SearchCategories ***/
ALTER TABLE [dbo].[SearchRevitCategories]  WITH CHECK ADD  CONSTRAINT [FK_SearchRevitCategories_Searches_searchId] FOREIGN KEY([searchId])
REFERENCES [dbo].[Searches] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[SearchRevitCategories] CHECK CONSTRAINT [FK_SearchRevitCategories_Searches_searchId]

/*** Alter SearchTags ***/
ALTER TABLE [dbo].[SearchTags]  WITH CHECK ADD  CONSTRAINT [FK_SearchTags_Searches_searchId] FOREIGN KEY([searchId])
REFERENCES [dbo].[Searches] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[SearchTags] CHECK CONSTRAINT [FK_SearchTags_Searches_searchId]

/*** Alter Tags ***/
ALTER TABLE [dbo].[Tags]  WITH CHECK ADD  CONSTRAINT [FK_Tags_Users_addedById] FOREIGN KEY([addedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[Tags] CHECK CONSTRAINT [FK_Tags_Users_addedById]

ALTER TABLE [dbo].[Tags]  WITH CHECK ADD  CONSTRAINT [FK_Tags_Users_updatedById] FOREIGN KEY([updatedById])
REFERENCES [dbo].[Users] ([id])

ALTER TABLE [dbo].[Tags] CHECK CONSTRAINT [FK_Tags_Users_updatedById]

/*** Alter UserFavoriteContents ***/
ALTER TABLE [dbo].[UserFavoriteContents]  WITH CHECK ADD  CONSTRAINT [FK_UserFavoriteContents_Contents_contentId] FOREIGN KEY([contentId])
REFERENCES [dbo].[Contents] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[UserFavoriteContents] CHECK CONSTRAINT [FK_UserFavoriteContents_Contents_contentId]

ALTER TABLE [dbo].[UserFavoriteContents]  WITH CHECK ADD  CONSTRAINT [FK_UserFavoriteContents_Users_userId] FOREIGN KEY([userId])
REFERENCES [dbo].[Users] ([id])
ON DELETE CASCADE

ALTER TABLE [dbo].[UserFavoriteContents] CHECK CONSTRAINT [FK_UserFavoriteContents_Users_userId]

/*** Alter Users ***/