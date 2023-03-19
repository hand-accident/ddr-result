<script>
    let className;
    export { className as class };
</script>

<div class="c {className}">
    <slot />
</div>

<style lang="postcss" module>
    .c {
        /* drawer drawer-end*/
        @apply grid overflow-hidden w-full;
        height: 100vh;
        height: 100dvh;
        direction: rtl;
    }
</style>
