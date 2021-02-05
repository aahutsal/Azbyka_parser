<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output indent="yes" method="xml"/>

  <xsl:strip-space elements="*"/>

  <xsl:template match="//div[@class='article-single-content main-page-content']">
    <akafist>
      <title><xsl:value-of select="//div[@class='article-single-info']/h1/text()"/></title>
      <title-sample><xsl:value-of select="ul/li/a/text()"/></title-sample>

      <get-me-more-data-here/>
    </akafist>
  </xsl:template>

  <xsl:template match="text()">    
  </xsl:template>


</xsl:stylesheet>
