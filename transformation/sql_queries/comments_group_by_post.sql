SELECT 
	post_id
	,title
	,body
	,url
	,author_post
	,created_post
	,permalink_post
	,flair
	,COUNT(DISTINCT comment_id) AS nb_comment
	,SUM(CASE WHEN sentiment_cat == 'Positive' THEN 1 ELSE 0 END) AS nb_positive
	,SUM(CASE WHEN sentiment_cat == 'Negative' THEN 1 ELSE 0 END) AS nb_negative
	,SUM(CASE WHEN sentiment_cat == 'Neutral' THEN 1 ELSE 0 END) AS nb_neutral
	,SUM(CASE WHEN sentiment_cat == 'Positive' THEN 1 ELSE 0 END) - SUM(CASE WHEN sentiment_cat == 'Negative' THEN 1 ELSE 0 END) AS sentiment_cat_ratio
	,SUM(sentiment_num) AS sentiment_num_ratio
FROM france_transformed
GROUP BY
	post_id
	,title
	,body
	,url
	,author_post
	,created_post
	,permalink_post
	,flair

#Done in 33290ms