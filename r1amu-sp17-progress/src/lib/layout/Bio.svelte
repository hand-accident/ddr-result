<script>
    import Avatar from "../cell/Avatar.svelte";
    import AvatarInner12r from "../cell/AvatarInner12r.svelte";
    export let src;
</script>

<Avatar class="">
    <AvatarInner12r class="">
        <img {src} alt="icon" />
    </AvatarInner12r>
</Avatar>
<p class="l"><slot /></p>

<style lang="postcss" module>
    .l {
        @apply pl-1;
    }
</style>
