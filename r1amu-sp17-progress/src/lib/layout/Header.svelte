<script>
    import ButtonInfoLabel from "../cell/ButtonInfoLabel.svelte";
    import Hero300 from "../cell/Hero300.svelte";
    import HeroContent from "../cell/HeroContent.svelte";
    import Paragraph from "../cell/Paragraph.svelte";
    import TitleText from "../cell/TitleText.svelte";
</script>

<Hero300 class="">
    <HeroContent class="">
        <TitleText class=""><slot name="title" /></TitleText>
        <Paragraph class=""><slot name="update" /></Paragraph>
        <ButtonInfoLabel class="" for="config">open config</ButtonInfoLabel>
    </HeroContent>
</Hero300>

<slot />

<style lang="postcss" module>
</style>
